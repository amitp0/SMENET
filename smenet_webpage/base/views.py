from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# functions or classes where we write our buisness logics

rooms=[
    {'id':1,'name':'SOFTWARE DEVOPS'},
    {'id':2,'name':'DATA SCIENTISTS'},
    {'id':3,'name':'ANDROID DEVOPS'},
    {'id':4,'name':'IOS DEVOP'},
]

def home(request):
    context_dic={'rooms':rooms}
    return render(request,'base/home.html',context_dic)


def profile(request,pk):
    room = None
    for i in rooms:
        if i['id']==int(pk):
            room=i
    context={'room':room} 
    return render(request,'base/profile.html',context)
