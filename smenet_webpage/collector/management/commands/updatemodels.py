from django.core.management.base import BaseCommand
from django.db import models
import pandas as pd
from collector.models import Companies
class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df=pd.read_csv('CSV3.csv')
        for Name,location,domain,email,password,phone in zip(df.Company_Name,df.Company_location,df.Comapny_domain,df.Email,df.Password,df.Phone_no):
            models=Companies(Company_Name=Name,Company_location=location,Company_domain=domain,Email=email,Password=password,Phone_no=phone)
            models.save()


