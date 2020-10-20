from rest_framework import serializers
from rest_framework.settings import api_settings

from sentence import models
from user.models import User
from user.serializers.user_serializers import UserSearchSerializer


class SentenceSerializer(serializers.Serializer):
    create_user = serializers.IntegerField(required=False, source='create_user_id')
    update_user = serializers.IntegerField(required=False, source='update_user_id')

    content = serializers.CharField(max_length=1500, required=True)
    from_by = serializers.CharField(max_length=50, required=True, allow_null=True)
    from_who = serializers.CharField(max_length=50, required=True, allow_null=True)
    creator = serializers.CharField(max_length=50, required=True)
    uuid = serializers.UUIDField(format='hex_verbose', required=True)

    type = serializers.IntegerField(allow_null=False, required=True, source='type_id')

    def validate_uuid(self, value):
        if models.Content.objects.filter(uuid=value).exists():
            raise serializers.ValidationError('uuid重复')
        return value

    def create(self, validated_data):
        return models.Content.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class SentenceTypeSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=20, required=True)
    code = serializers.CharField(max_length=20, required=True)

    def validate_name(self, value):
        if models.ContentType.objects.filter(name=value).exists():
            raise serializers.ValidationError('类型名称重复')
        return value

    def validate_code(self, value):
        if models.ContentType.objects.filter(code=value).exists():
            raise serializers.ValidationError('类型code重复')
        return value

    def create(self, validated_data):
        return models.ContentType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return


class ContentSerializer(serializers.ModelSerializer):
    type = SentenceTypeSerializer()
    create_date = serializers.DateTimeField(read_only=True, format=api_settings.DATETIME_FORMAT)

    def get_create_date(self, obj):
        return '****'

    class Meta:
        model = models.Content
        fields = ['content', 'from_by', 'from_who', 'creator', 'uuid', 'type', 'create_date']
        depth = 1
