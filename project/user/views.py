from tkinter import N
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import EmployeeForm, UserRegisterForm
from .models import Company, Employee
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel


def top_recommend(request):
    d2 = pd.read_csv(r"C:\Users\admin\Desktop\dj-sme\project\user\media\database.csv")
    d2 = d2.nlargest(6, ["ratings"])
    d2 = pd.DataFrame(d2)
    n1=d2['name']
    n2=d2['industry_new']
    n3=d2['rating']
    tp=tuple(zip(n1,n2,n3))
    return tp


def new_adds(request):
    d2 = pd.read_csv(r"C:\Users\admin\Desktop\dj-sme\project\user\media\database.csv")
    d2 = d2.tail(6)
    d2 = pd.DataFrame(d2)
    n1=d2['name']
    n2=d2['industry_new']
    n3=d2['rating']
    tna=tuple(zip(n1,n2,n3))
    return tna


def give_recommendation(name):
    d2 = pd.read_csv(r"C:\Users\admin\Desktop\dj-sme\project\user\media\database.csv")
    tfv = TfidfVectorizer(
        min_df=1,
        max_features=None,
        strip_accents="unicode",
        analyzer="word",
        token_pattern=r"\w{1,}",
        ngram_range=(1, 3),
        stop_words="english",
    )
    tfv_matrix = tfv.fit_transform(d2["r_lemmatized"])
    sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
    l = []
    ir= []
    r= []
    index = d2[d2["name"] == name].index[0]
    sig_scores = list(enumerate(sig[index]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1:11]
    comp_indices = [i[0] for i in sig_scores]
    for i in comp_indices:
        val = d2["name"].iloc[i]
        ind= d2["industry_new"].iloc[i]
        rating=d2["rating"].iloc[i]
        l.append(val)
        ir.append(str(ind))
        r.append(rating)
    tp=tuple(zip(l,ir,r))
    return tp

def give_rec2(username):
    r=Company.objects.get(username=username)
    print(r.company_domain)
    dataframe=pd.read_csv(r'C:\Users\admin\Desktop\dj-sme\project\user\media\database.csv')
    rslt_df = dataframe[dataframe['industry_new'] == r.company_domain]
    rslt_df=pd.DataFrame(rslt_df)
    rslt_df=rslt_df.head(11)
    name=rslt_df['name']
    ind=rslt_df['industry_new']
    rat=rslt_df['rating']
    pred=tuple(zip(name,ind,rat))
    return pred

def index(request):
    return render(request, "user/index.html")


@login_required
def dashboard(request):
    
    if request.user.is_authenticated:
        username = request.user.username
    else:
        print("::::::::::::::::::::")
    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"+username+";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")

    try:
        pred = give_recommendation(username)
        print("INTERNAL RECC")
        print("ooooooooooooooooooooooooooooooo"+"Not in dataset"+"ooooooooooooooooooooooooooooooo")
    except:
        pred=give_rec2(username)
        print("///////")

    

        


    newad=new_adds(request)
    toprec=top_recommend(request)
    print("************************************************************")
    context = {'pred': pred,'new':newad,'top':toprec}
    return render(request, 'user/dashboard.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            company_domain = form.cleaned_data.get("company_domain")
            company_location = form.cleaned_data.get("company_location")
            phone_no = form.cleaned_data.get("phone_no")
            c = Company(
                username=username,
                email=email,
                company_domain=company_domain,
                company_location=company_location,
                phone_no=phone_no,
            )
            c.save()
            return redirect("signin")
    else:
        form = UserRegisterForm()
    return render(request, "user/signup.html", {"form": form})


def Login(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f" welcome {username} !!")
            return redirect("dashboard")
        else:
            messages.info(request, f"account does not exit plz sign in")
    form = AuthenticationForm()
    return render(request, "user/signin.html", {"login_form": form})


@login_required
def employee_dashboard(request):
    all_emp = Employee.objects.all()
    return render(request, "user/emp.html", {"d": all_emp})


def recommend(request):
    try:
        pred = give_recommendation("Merx Global")
        print(pred)
        context = {"a": pred}
        return render(request, "user/result.html", context)
    except:
        print("Company does not exist in database")
        return redirect("signup")

def user_page(request,username):
    r=Company.objects.get(username=username)
    return render(request,)


@login_required
def addEmployee(request):
    sample_instance = Company.objects.get(username=request.user.username)
    value_of_name = sample_instance.comp_id
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
            form= EmployeeForm()
    return render(request,'user/s.html',{'form':form,'comp_id':value_of_name})

@login_required
def show(request):
    sample_instance = Company.objects.get(username=request.user.username)
    value_of_name = sample_instance.comp_id
    print(value_of_name)
    # print("fthdhdhhx")
    employees = Employee.objects.filter(company_id=value_of_name)  
    return render(request,"user/show.html",{'employees':employees}) 

@login_required
def edit(request, id):  
    employee = Employee.objects.get(emp_id=id)  
    return render(request,'user/edit.html', {'employee':employee})

@login_required
def update(request, id):  
    employee = Employee.objects.get(emp_id=id)  
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'user/edit.html', {'employee': employee})  

@login_required
def delete(request, id):  
    employee = Employee.objects.get(emp_id=id)  
    employee.delete()  
    return redirect("/show")  

@login_required
def public_view(request, username): 
    print(username)
    try:
        sample_instance = Company.objects.get(username=username)
        value_of_name = sample_instance.comp_id
        comp_email=sample_instance.email
        comp_domain=sample_instance.company_domain
        comp_location=sample_instance.company_location
        comp_phone=sample_instance.phone_no
        employees = Employee.objects.filter(company_id=value_of_name)
        return render(request,"user/showpublic.html",{'employees':employees,'comp_name':username,'comp_email':comp_email,'comp_domain':comp_domain,'comp_phone':comp_phone,'comp_location':comp_location})  

    except:
        # value_of_name = sample_instance.comp_id
        # employees = Employee.objects.filter(company_id=value_of_name)
        return render(request,"user/showpublic_notreg.html",{'comp_name':username,})  
    