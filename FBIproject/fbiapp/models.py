from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class Options(models.Model):
    option_id = models.IntegerField(primary_key=True)
    op1 = models.CharField(max_length=50, blank=True, null=True)
    op2 = models.CharField(max_length=50, blank=True, null=True)
    op3 = models.CharField(max_length=50, blank=True, null=True)
    op4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Options'


class Questions(models.Model):
    question_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=50)
    option = models.ForeignKey(Options, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Questions'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, name, age, keyword, state, environment, cycle,  password = None):
        user = self.model(
            user_id=user_id,
            name=None,
            age=0,
            keyword=None,
            state=0,
            environment =0,
            cycle =0,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password):
        user = self.create_user(
            password=password,
            user_id=user_id,
            name=None,
            age=0,
            keyword=None,
            state=0,
            environment =0,
            cycle =0,

        )
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    object = CustomUserManager()
    
    user_id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=100, blank=True, null=True)
    keyword = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    environment = models.CharField(max_length=100, blank=True, null=True)
    cycle = models.CharField(max_length=100, blank=True, null=True)
    
    is_active = models.IntegerField(blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    last_login = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'user',
        verbose_name_plural = 'users'
        db_table = 'user'


    def __str__(self):
        return self.user_id

    def get_full_name(self):
        return self.user_id

    def get_short_name(self):
        return self.user_id

    @property
    def is_staff(self):
        return self.is_superuser
    
    USERNAME_FIELD = 'user_id'



class UserGroups(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    group = models.ForeignKey('fbiapp.AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)


class UserUserPermissions(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    permission = models.ForeignKey('fbiapp.AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_permissions'
        unique_together = (('user', 'permission'),)
