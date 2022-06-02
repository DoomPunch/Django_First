# Generated by Django 4.0 on 2022-06-02 06:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, db_column='Role', max_length=200, null=True)),
                ('is_valid', models.CharField(blank=True, db_column='IsValid', max_length=10, null=True)),
                ('create_by', models.IntegerField(blank=True, db_column='CreateBy', null=True)),
                ('create_time', models.DateTimeField(blank=True, db_column='CreateTime', default=django.utils.timezone.now, null=True)),
                ('modified_by', models.IntegerField(blank=True, db_column='ModifiedBy', null=True)),
            ],
            options={
                'db_table': 'sys_role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(blank=True, db_column='LoginName', max_length=50, null=True)),
                ('login_pwd', models.CharField(blank=True, db_column='Login_pwd', max_length=50, null=True)),
                ('user_name', models.CharField(blank=True, db_column='UserName', max_length=50, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=10, null=True)),
                ('is_valid', models.CharField(blank=True, db_column='IsValid', max_length=10, null=True)),
                ('create_by', models.IntegerField(blank=True, db_column='CreateBy', null=True)),
                ('create_time', models.DateTimeField(blank=True, db_column='CreateTime', default=django.utils.timezone.now, null=True)),
                ('modified_by', models.IntegerField(blank=True, db_column='ModifiedBy', null=True)),
            ],
            options={
                'db_table': 'sys_user',
                'ordering': ('create_time',),
            },
        ),
    ]
