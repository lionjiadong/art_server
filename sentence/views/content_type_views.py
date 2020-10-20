import time

from rest_framework.views import APIView
from rest_framework.response import Response
from sentence.serializers import content_serializers
from sentence import models
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.
import django_filters.rest_framework
from rest_framework import generics


# class ProductFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='iexact')
#
#     class Meta:
#         model = models.ContentType
#         fields = ['name', 'code']


class ContentTypeList(generics.ListCreateAPIView):
    # authentication_classes = []
    # # search_fields = ['name', 'code']
    # serializer_class = content_serializers.SentenceTypeSerializer
    # queryset = models.ContentType.objects.all()
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # # filterset_fields = ['name', 'code']
    # filterset_class = ProductFilter

    def dispatch(self, request, *args, **kwargs):
        return super(ContentTypeList, self).dispatch(request, *args, **kwargs)

    # @method_decorator(cache_page(60))
    def get(self, request, *args, **kwargs):
        # time.sleep()
        sentence_types = models.ContentType.objects.all().order_by('sequence')
        serializer = content_serializers.SentenceTypeSerializer(sentence_types, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        type_ser = content_serializers.SentenceTypeSerializer(data=data)
        type_ser.is_valid(raise_exception=True)
        type_ser.save()
        return Response(type_ser.data)


class ContentTypeDetail(APIView):

    def dispatch(self, request, *args, **kwargs):
        return super(ContentTypeDetail, self).dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return models.ContentType.objects.get(pk=pk)
        except models.ContentType.DoesNotExist:
            raise Http404

    @method_decorator(cache_page(60))
    def get(self, request, pk, *args, **kwargs):
        sentence = self.get_object(pk)
        serializer = content_serializers.SentenceTypeSerializer(sentence)
        return Response(serializer.data)

    def patch(self, request, pk):
        return Response(status=200)

    def delete(self, request, pk):
        models.ContentType.objects.get(pk=pk).delete()
        return Response(status=200)
