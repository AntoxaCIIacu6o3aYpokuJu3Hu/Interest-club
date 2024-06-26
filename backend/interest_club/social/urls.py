from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from social import views

urlpatterns = [
    path('groups/', views.SocialGroupList.as_view()),
    path('groups/membership/', views.SocialGroupMembership.as_view()),
    path('groups/<str:pk>/', views.SocialGroupDetail.as_view()),
    path('records/', views.GroupRecordList.as_view()),
    path('records/<str:pk>/', views.GroupRecordDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<str:pk>/', views.CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)