from rest_framework import serializers
from user import models
import logging

logger = logging.getLogger(__name__)


class UserCreateSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True,
                                     min_length=6,
                                     required=True,
                                     error_messages={
                                         'min_length': '密码长度最小6位',
                                         'required': '未提供用登录密码'
                                     })
    email = serializers.EmailField(max_length=50,
                                   required=True,
                                   error_messages={
                                       'required': '未提供用账户邮箱'
                                   })

    def validate_email(self, value):
        if models.User.objects.filter(email=value).exists():
            raise serializers.ValidationError('用户用户邮箱重复')
        return value

    def create(self, validated_data):
        return models.User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        pass


class UserSearchSerializer(serializers.ModelSerializer):
    # id = serializers.PrimaryKeyRelatedField(read_only=True)
    # create_date = serializers.DateTimeField(auto_now_add=True)
    # update_date = serializers.DateTimeField(auto_now=True)
    # is_active = serializers.BooleanField(default=True)
    # uid = serializers.UUIDField(verbose_name='uid')
    # email = serializers.EmailField(verbose_name='邮箱')

    class Meta:
        model = models.User

        fields = ['id', 'email', 'uid']
