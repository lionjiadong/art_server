from django.db import models
from django.conf import settings
import uuid


class ContentType(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.SET_NULL, null=True)
    update_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=20, null=False, unique=True)
    code = models.CharField(max_length=20, null=False, unique=True)
    sequence = models.IntegerField(null=True)

    class Meta:
        db_table = 'sentence_content_type'


class Content(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.SET_NULL, null=True)
    update_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.SET_NULL, null=True)

    content = models.CharField(verbose_name='内容', max_length=1500, null=False)
    from_by = models.CharField(verbose_name='出自哪里', max_length=50, null=True)
    from_who = models.CharField(verbose_name='出自谁', max_length=50, null=True)
    creator = models.CharField(verbose_name='创建人', max_length=50, null=False)
    uuid = models.UUIDField(null=False, unique=True, default=uuid.uuid4())
    type = models.ForeignKey(ContentType, related_name='+', on_delete=models.SET_NULL, null=True)
    image = models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')

    class Meta:
        db_table = 'sentence_content'
