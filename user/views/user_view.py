from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from user import models
from user.serializers import user_serializers, user_info_serializers
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# Create your views here.
class UserList(APIView):

    def dispatch(self, request, *args, **kwargs):
        return super(UserList, self).dispatch(request, *args, **kwargs)

    @method_decorator(cache_page(60))
    def get(self, request, *args, **kwargs):
        user_list = models.User.objects.all()
        serializer = user_serializers.UserSearchSerializer(user_list, many=True)
        return Response(serializer.data)


class UserDetail(APIView):

    def dispatch(self, request, *args, **kwargs):
        return super(UserDetail, self).dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return models.UserInfo.objects.get(pk=pk)
        except models.UserInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user_info = self.get_object(pk)
        serializer = user_info_serializers.UserInfoSerializer(user_info)
        return Response(serializer.data)
