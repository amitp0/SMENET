from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Layout,Field
from crispy_forms.helper import FormHelper
from numpy import true_divide
from user.models import Employee


class UserRegisterForm(UserCreationForm):
	domains=['Aerospace & Defense', 'Agriculture', 'Agriculture and Extraction', 'Arts, Entertainment & Recreation', 'Auto', 'Automotive', 'Computers and Electronics', 'Construction', 'Construction & Facilities Services', 'Consulting and Business Services', 'Consumer Goods and Services', 'Education', 'Education and Schools', 'Energy, Mining & Utilities', 'Financial Services', 'Food and Beverages', 'Government & Public Administration', 'Health Care', 'Healthcare', 'Hotels & Travel Accommodation', 'Human Resources & Staffing', 'Industrial Manufacturing', 'Information Technology', 'Insurance', 'Internet and Software', 'Legal', 'Management & Consulting', 'Manufacturing', 'Media & Communication', 'Nonprofit & NGO', 'Organization', 'Personal Consumer Services', 'Pharmaceutical & Biotechnology', 'Real Estate', 'Restaurants & Food Service', 'Restaurants, Travel and Leisure', 'Retail', 'Retail & Wholesale', 'Telecommunications', 'Transport and Freight', 'Transportation & Logistics']
	username = forms.CharField(required=True, label="Company Name")
	company_domain = forms.ChoiceField( required=True,choices=[(" ", "Select Domain")]+[(x, x) for x in domains])
	company_location = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	phone_no = forms.IntegerField(required=True)
	
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_no', 'company_location',
                  'company_domain', 'password1', 'password2']

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.company_domain = self.cleaned_data["company_domain"]
		user.company_location = self.cleaned_data["company_location"]
		if commit:
			user.save()
		return user

class EmployeeForm(forms.ModelForm):
	emp_id=forms.IntegerField(required=True)
	emp_name=forms.CharField(required=True)
	company_id=forms.IntegerField(required=True)
	domain=forms.CharField(required=True)
	ready_to_relocate=forms.BooleanField(required=True)
	current_loc=forms.CharField(required=True)
	resume_link=forms.URLField(required=False)
	notice_period=forms.DateField(required=True)
	laidoffdate=forms.DateField(required=True)

	class Meta:
		model=Employee
		fields=['emp_id','emp_name','company_id','domain','ready_to_relocate','current_loc','resume_link','notice_period','laidoffdate']
		
	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	self.helper = FormHelper()
	# 	self.helper.layout = Layout(Field('domain', type='hidden'))