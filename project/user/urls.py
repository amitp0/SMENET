from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import activate

urlpatterns = [
		path('', views.index, name ='index'),
		path('activate/<uidb64>/<token>/',activate, name='activate'),
]
