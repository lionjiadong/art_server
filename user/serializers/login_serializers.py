from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=50, required=True, error_messages={'required': '未提供用登录邮箱'})
    password = serializers.CharField(min_length=6, required=True, error_messages={'required': '未提供用登录密码'})
    remember = serializers.BooleanField(required=True, label='123', error_messages={'required': 'remember参数未提供'})
