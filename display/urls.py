from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.home),
    path('sendemail/', v.sendemail),
]