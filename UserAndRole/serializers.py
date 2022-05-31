from rest_framework import serializers
from UserAndRole.models import User, Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'login_name', 'login_pwd', 'user_name', 'gender', '')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ()
