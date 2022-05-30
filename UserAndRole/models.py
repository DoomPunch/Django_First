from django.db import models

# Create your models here.


class User(models.Model):
    login_name = models.CharField(max_length=50, db_column='LoginName')
    login_pwd = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    is_valid = models.CharField(max_length=1)
    create_by = models.IntegerField()
    create_time = models.DateTimeField()
    modified_by = models.IntegerField()

    class Meta:
        db_table = 'sys_user'


class Role(models.Model):

    class Meta:
        db_table = 'sys_role'
