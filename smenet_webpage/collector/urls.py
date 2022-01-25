from django.urls import path
from . import views
#  . is current dir



# set our routes in a list
urlpatterns=[
    path('dashboard/',views.dashboard_view,name="dashboard"),
    
    
    
]
