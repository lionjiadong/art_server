import time

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from sentence import models
from sentence.serializers import content_serializers
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class ContentList(APIView):
    # authentication_classes = [Sess]
    throttle_classes = [AnonRateThrottle]

    def dispatch(self, request, *args, **kwargs):
        return super(ContentList, self).dispatch(request, *args, **kwargs)

    # @method_decorator(cache_page(10))
    def get(self, request, *args, **kwargs):
        time.sleep(0.2)
        if 'type_list[]' in request.query_params.keys():
            params_type_list = request.query_params.getlist('type_list[]')
            if len(params_type_list) == 1:
                type_list = '(%s)' % params_type_list[0]
            else:
                type_list = tuple(params_type_list)
        else:
            type_list = tuple([types.id for types in models.ContentType.objects.all()])
        content_sql = 'SELECT * FROM sentence_content where type_id in {type_list} ORDER BY RAND() LIMIT 1'.format(
            type_list=type_list)
        content = models.Content.objects.raw(content_sql)
        contents_ser = content_serializers.ContentSerializer(content[0])
        return Response(contents_ser.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['create_user'] = request.user.id
        data['update_user'] = request.user.id
        content_ser = content_serializers.SentenceSerializer(data=data)
        content_ser.is_valid(raise_exception=True)
        content_obj = content_ser.save()
        return Response(content_serializers.ContentSerializer(content_obj).data)


class ContentDetail(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super(ContentDetail, self).dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return models.Content.objects.get(pk=pk)
        except models.Content.DoesNotExist:
            raise Http404

    @method_decorator(cache_page(60))
    def get(self, request, pk, *args, **kwargs):
        sentence = self.get_object(pk)
        serializer = content_serializers.SentenceSerializer(sentence)
        return Response(serializer.data)

    def patch(self, request, pk):
        print(request.data)
        print(request.FILES)
        print(request.FILES['image'])
        print(request.FILES.getlist('image'))
        try:
            content_obj = models.Content.objects.get(pk=pk)
            content_obj.image = request.FILES['image']
            content_obj.save()
            return Response(status=200)
        except models.Content.DoesNotExist:
            raise Http404
