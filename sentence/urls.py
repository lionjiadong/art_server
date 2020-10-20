from django.urls import path
from sentence import views
urlpatterns = [
    path('content_types/', views.content_type_views.ContentTypeList.as_view()),
    path('content_types/<int:pk>/', views.content_type_views.ContentTypeDetail.as_view()),

    path('contents/', views.content_views.ContentList.as_view()),
    path('contents/<int:pk>/', views.content_views.ContentDetail.as_view()),
]
