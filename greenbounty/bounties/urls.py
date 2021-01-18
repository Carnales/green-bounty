from django.urls import path
from . import views

urlpatterns = [
    path('', views.bounties, name="bounties"),
    path('account/', views.account, name="account"),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('logout/', views.logout, name="logout"),
    path('create/', views.add_bounty, name="create"),
    path('submit/', views.submit, name="submit"),
    path('submitted/', views.submitted, name="submitted")
]