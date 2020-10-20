from django.urls import path
from user import views
urlpatterns = [
    path('login/', views.log_view.LogView.as_view()),
    path('logout/', views.log_view.LogView.as_view()),

    path('user_infos/', views.user_info_view.UserInfoList.as_view()),
    path('user_infos/<int:pk>/', views.user_info_view.UserInfoDetail.as_view()),

    path('users/', views.user_view.UserList.as_view()),
    path('users/<int:pk>/', views.user_view.UserDetail.as_view()),
]
