"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from user import views as user_view
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('signin/', user_view.Login, name ='signin'),
    path('signup/', user_view.register, name ='signup'),
    path('dashboard/', user_view.dashboard, name ='dashboard'),
    path('emp/', user_view.employee_dashboard, name ='e_dashboard'),
    path('recommend/', user_view.recommend, name ='e_dashboard'),
    path("user/<str:username>/",user_view.user_page, name="user_page"),
    path('empAdd/', user_view.addEmployee, name ='e_dashboard'),
    path("show/",user_view.show,name="show"),
    path("edit/<int:id>",user_view.edit,name="edit"),
    path("update/<int:id>",user_view.update,name="update"),
    path("delete/<int:id>",user_view.delete,name="delete"),

]
