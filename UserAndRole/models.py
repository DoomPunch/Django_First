from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    login_name = models.CharField(max_length=50, db_column='LoginName')
    login_pwd = models.CharField(max_length=50, db_column='Login_pwd')
    user_name = models.CharField(max_length=50, db_column='UserName')
    gender = models.CharField(max_length=10, db_column='Gender')
    is_valid = models.CharField(max_length=10, db_column='IsValid')
    create_by = models.IntegerField(default=0, db_column='CreateBy')
    create_time = models.DateTimeField(default=timezone.now, db_column='CreateTime')
    modified_by = models.IntegerField(default=0, db_column='ModifiedBy')

    class Meta:
        db_table = 'sys_user'
        ordering = ('create_time',)


class Role(models.Model):
    role = models.CharField(max_length=200, db_column='Role')
    is_valid = models.CharField(max_length=10, db_column='IsValid', )
    create_by = models.IntegerField(default=0, db_column='CreateBy')
    create_time = models.DateTimeField(db_column='CreateTime', default=timezone.now,)
    modified_by = models.IntegerField(default=0, db_column='ModifiedBy')

    class Meta:
        db_table = 'sys_role'
