from django.shortcuts import render
# from .models import Log
# Create your views here.
from .models import Companies

def dashboard_view(request):
    
    # obj=Log.objects.get(id=1)
    # context={
    #     'title':obj.
    # }
    Companies_ob=Companies.objects.all().order_by('-id')[:50]
    return render(request,'collector/dashboard.html',{'Companies_ob':Companies_ob})

