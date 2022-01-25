from django.urls import path
from . import views
#  . is current dir



# set our routes in a list
urlpatterns=[
    path('home/',views.home,name="home"),
    path('profile/<str:pk>',views.profile,name="profile"),
]