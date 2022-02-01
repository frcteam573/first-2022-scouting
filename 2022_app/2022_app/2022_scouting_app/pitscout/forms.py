from django import forms
from .models import pitscout

class pitscout_form(forms.ModelForm):
	class Meta:
		model = pitscout
		exclude = []