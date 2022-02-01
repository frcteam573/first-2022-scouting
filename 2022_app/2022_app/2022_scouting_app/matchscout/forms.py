from django import forms
from .models import matchscout

class matchscout_form(forms.ModelForm):
	class Meta:
		model = matchscout
		exclude = []