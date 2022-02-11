from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from .models import Company, Employee
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
    return d2["name"]


def new_adds(request):
    d2 = pd.read_csv(r"C:\Users\admin\Desktop\dj-sme\project\user\media\database.csv")
    d2 = d2.tail(6)
    return d2["name"]


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
    index = d2[d2["name"] == name].index[0]
    sig_scores = list(enumerate(sig[index]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1:11]
    comp_indices = [i[0] for i in sig_scores]
    for i in comp_indices:
        val = d2["name"].iloc[i]
        l.append(val)
    return l


# on hitting url endpoint home/recommend will be redirected here


def index(request):
    return render(request, "user/index.html")


@login_required
def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        print("::::::::::::::::::::")
    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"+username)

    try:
        pred = give_recommendation(username)
    except:
        print("ooooooooooooooooooooooooooooooo"+"Not in dataset")

        
    try:
        r=Company.objects.get(username=username)
        print(r.company_domain)
        dataframe=pd.read_csv(r'C:\Users\admin\Desktop\dj-sme\project\user\media\result.csv')
        rslt_df = dataframe[dataframe['industry'] == r.company_domain]
        rslt_df=pd.DataFrame(rslt_df)
        rslt_df=rslt_df.head(11)
        pred=rslt_df['name']
        print(pred)
    except:
        print("/////////////////////")


    newad=new_adds(request)
    toprec=top_recommend(request)
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
