from rest_framework import serializers
from .user_serializers import UserCreateSerializer
from user import models


class UserInfoSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    nickname = serializers.CharField(label='昵称', max_length=20)
    user_id = serializers.IntegerField(write_only=True)
    user = UserCreateSerializer(read_only=True)

    def create(self, validated_data):
        return models.UserInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


