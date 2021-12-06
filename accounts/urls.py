from .views import RegistrationAPIView
from django.urls import path

urlpatterns = [
    path('', RegistrationAPIView.as_view())

]