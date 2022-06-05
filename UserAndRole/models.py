from django.db import models
from django.utils import timezone

# Create your models here.


__all__ = ['User', 'Role', 'Menu', 'RoleForUser', 'RoleForMenu']


class User(models.Model):
    login_name = models.CharField(max_length=50, db_column='LoginName', null=True, blank=True, help_text='登录账号')
    login_pwd = models.CharField(max_length=50, db_column='Login_pwd', null=True, blank=True, help_text='登录密码')
    user_name = models.CharField(max_length=50, db_column='UserName', null=True, blank=True)
    gender = models.CharField(max_length=1, db_column='Gender', null=True, blank=True)
    is_valid = models.CharField(max_length=1, db_column='IsValid', null=True, blank=True)
    create_by = models.IntegerField(db_column='CreateBy', null=True, blank=True)
    create_time = models.DateTimeField(default=timezone.now, db_column='CreateTime', null=True, blank=True)
    modified_by = models.IntegerField(db_column='ModifiedBy', null=True, blank=True)
    modified_time = models.DateTimeField(db_column='ModifiedTime', auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'sys_user'
        ordering = ('create_time',)


class Role(models.Model):
    role = models.CharField(max_length=200, db_column='Role', null=True, blank=True)
    is_valid = models.IntegerField(db_column='IsValid', null=True, blank=True)
    create_by = models.IntegerField(db_column='CreateBy', null=True, blank=True)
    create_time = models.DateTimeField(db_column='CreateTime', default=timezone.now, null=True, blank=True)
    modified_by = models.IntegerField(db_column='ModifiedBy', null=True, blank=True)
    modified_time = models.DateTimeField(db_column='ModifiedTime', auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'sys_role'


class Menu(models.Model):
    menu_name = models.CharField(max_length=200, db_column='MenuName', null=True, blank=True)
    parent_id = models.IntegerField(db_column='ParentId', null=True, blank=True)
    is_valid = models.IntegerField(db_column='IsValid', null=True, blank=True)
    create_by = models.IntegerField(db_column='CreateBy', null=True, blank=True)
    create_time = models.DateTimeField(db_column='CreateTime', default=timezone.now, null=True, blank=True)
    modified_by = models.IntegerField(db_column='ModifiedBy', null=True, blank=True)
    modified_time = models.DateTimeField(db_column='ModifiedTime', auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'sys_menu'


class RoleForUser(models.Model):
    user_id = models.IntegerField(db_column='UserId', null=True, blank=True)
    role_id = models.IntegerField(db_column='RoleId', null=True, blank=True)

    class Meta:
        db_table = 'sys_role_for_user'


class RoleForMenu(models.Model):
    role_id = models.IntegerField(db_column='RoleId', null=True, blank=True)
    menu_id = models.IntegerField(db_column='MenuId', null=True, blank=True)

    class Meta:
        db_table = 'sys_role_for_menu'
