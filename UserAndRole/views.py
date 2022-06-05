from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from UserAndRole.models import User, Role
from UserAndRole.serializers import UserSerializer, RoleSerializer

# Create your views here.


@api_view(['GET', 'POST', 'PUT'])
@csrf_exempt
def user_list(request):
    """
    :param request:请求
    :return: 返回所有的 user
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
