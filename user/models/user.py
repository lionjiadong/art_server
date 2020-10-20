from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from django.db import models


class UserManage(BaseUserManager):

    def _create_user(self, **extra_fields):
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(**extra_fields)
        user.set_password(extra_fields['password'])
        user.save(using=self._db)
        return user

    def create_user(self, **extra_fields):
        return self._create_user(**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    uid = models.UUIDField(verbose_name='uid', default=uuid.uuid4, unique=True)
    email = models.EmailField(verbose_name='邮箱', max_length=50, unique=True)

    objects = UserManage()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['uid']
    EMAIL_FIELD = 'email'
