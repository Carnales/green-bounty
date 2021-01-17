from django.urls import path
from . import views

urlpatterns = [
    path('', views.bounties, name="bounties"),
]