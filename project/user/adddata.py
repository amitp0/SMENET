import csv, sys, os, django

project_dir = r"C:\Users\admin\Desktop\dj-sme\project"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
import django
django.setup()
from django.contrib.auth import authenticate
from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()
# User.objects.all().delete()
file = 'datao.csv'

data = csv.reader(open(file), delimiter=",")
for row in data:
    if row[0] != "Number":
        Post=User()
        Post.username = row[0]
        Post.set_password(row[1])
        Post.email="abc@example.com"
        Post.is_superuser = "0"
        Post.is_staff = "1"
        Post.is_active = "1"
        Post.save()
