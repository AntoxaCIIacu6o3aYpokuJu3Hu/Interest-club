from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from social import views

urlpatterns = [
    path('groups/', views.SocialGroupList.as_view()),
    path('groups/<str:pk>/', views.SocialGroupDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)