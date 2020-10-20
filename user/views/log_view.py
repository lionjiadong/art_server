from django.shortcuts import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import login_serializers


class LogView(APIView):
    authentication_classes = []

    def dispatch(self, request, *args, **kwargs):
        return super(LogView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        login_data = login_serializers.LoginSerializer(data=request.data)
        login_data.is_valid(raise_exception=True)
        user = authenticate(request, username=request.data['email'], password=request.data['password'])
        if user:
            login(request, user)
            if request.data['remember']:
                request.session.set_expiry(60 * 60 * 24 * 30)  # 30天
            return Response(status=200)
        else:
            return Response('账号或密码错误,请重试!', status=401)

    def put(self, request, *args, **kwargs):
        logout(request)
        return HttpResponse(status=200)
