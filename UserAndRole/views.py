from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from UserAndRole.models import User, Role
from UserAndRole.serializers import UserSerializer, RoleSerializer

# Create your views here.
