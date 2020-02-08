from django.shortcuts import render

from .forms import pitscout_form
from .models import pitscout

# Create your views here.

def pitscout(request):

	if request.method == 'POST':
		form = pitscout_form(request.POST)
		
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			form.save_m2m()
	
	form = pitscout_form()
	return render(request, 'pitscout.html', {'form': form})

