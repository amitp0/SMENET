from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
