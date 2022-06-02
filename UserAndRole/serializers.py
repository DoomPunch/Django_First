from rest_framework import serializers
from UserAndRole.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'login_name', 'login_pwd', 'user_name', 'gender', 'is_valid',
                  'create_by', 'create_time', 'modified_by', 'modified_time')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'is_valid', 'create_by', 'create_time', 'modified_by', 'modified_time')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'menu_name', 'parent_id', 'is_valid', 'create_by', 'create_time', 'modified_by',
                  'modified_time')


class RoleForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleForUser
        fields = ('id', 'user_id', 'role_id')


class RoleForMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleForMenu
        fields = ('id', 'role_id', 'menu_id')
