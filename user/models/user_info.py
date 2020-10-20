from django.db import models
from django.conf import settings


class UserInfo(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    nickname = models.CharField(verbose_name='昵称', max_length=20)
    birthday = models.DateField(null=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='user_info', on_delete=models.SET_NULL, null=True)
