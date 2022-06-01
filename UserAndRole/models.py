from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    login_name = models.CharField(max_length=50, db_column='LoginName', null=True, blank=True)
    login_pwd = models.CharField(max_length=50, db_column='Login_pwd', null=True, blank=True)
    user_name = models.CharField(max_length=50, db_column='UserName', null=True, blank=True)
    gender = models.CharField(max_length=10, db_column='Gender', null=True, blank=True)
    is_valid = models.CharField(max_length=10, db_column='IsValid', null=True, blank=True)
    create_by = models.IntegerField(db_column='CreateBy', null=True, blank=True)
    create_time = models.DateTimeField(default=timezone.now, db_column='CreateTime', null=True, blank=True)
    modified_by = models.IntegerField(db_column='ModifiedBy', null=True, blank=True)

    class Meta:
        db_table = 'sys_user'
        ordering = ('create_time',)


class Role(models.Model):
    role = models.CharField(max_length=200, db_column='Role', null=True, blank=True)
    is_valid = models.CharField(max_length=10, db_column='IsValid', null=True, blank=True)
    create_by = models.IntegerField(db_column='CreateBy', null=True, blank=True)
    create_time = models.DateTimeField(db_column='CreateTime', default=timezone.now, null=True, blank=True)
    modified_by = models.IntegerField(db_column='ModifiedBy', null=True, blank=True)

    class Meta:
        db_table = 'sys_role'
