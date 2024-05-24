from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path('registration/', views.Registration.as_view()),
    path('profile/', views.Profile.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)