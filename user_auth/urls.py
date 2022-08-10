
from django.urls import path
from .views import SignupView
urlpatterns = [
  path('create-user', SignupView.as_view()),
]