from django.db import models

# class Log(models.Model):
#     created = models.DateTimeField('date happened')
#     user_id = models.CharField(max_length=16)
#     content_id = models.CharField(max_length=16)
#     event = models.CharField(max_length=200)
#     session_id = models.CharField(max_length=128)

class Companies(models.Model):
    Company_Name=models.CharField(("Company_Name"),max_length=500)
    Company_location=models.CharField(("Company_location"),max_length=500)
    Company_domain=models.CharField(("Company_domain"),max_length=500)
    Email=models.EmailField(("Email"),max_length=500)
    Password=models.CharField(("Password"),max_length=500)
    Phone_no=models.IntegerField("Phone_no")
   
    def __str__(self):
        return f"File id:{self.id}"
    # Company Name 	Company location 	Company domain 	Email 	Password 	Phone no