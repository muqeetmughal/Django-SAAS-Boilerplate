from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('start-free-trial', start_trial, name="start-trial")
]
