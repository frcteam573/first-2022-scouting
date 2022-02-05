from django.shortcuts import render
from .forms import matchscout_form
from .models import matchscout
from pitscout.models import pitscout
from django.db.models import Avg, Max, Min, Q, Count
# Create your views here.

def index(request):
	return render(request, 'index.html')

def matchscout_view(request):
	if request.method == 'POST':
		form = matchscout_form(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			form.save_m2m()
	
	form = matchscout_form()
	return render(request, 'matchscout.html', {'form': form})



def teamsummary(request):
	if request.method == 'GET':
		team_number = request.GET.get('team_number', 0)
		results = matchscout.objects.filter(team_num = team_number)
		results_pit = pitscout.objects.filter(team_num = team_number)

		if team_number != 0:
		
			#autonomous
			a_upper_avg = round(list(results.aggregate(Avg('a_upper')).values())[0], 2)
			a_upper_max = round(list(results.aggregate(Max('a_upper')).values())[0], 2)
			a_upper_min = round(list(results.aggregate(Min('a_upper')).values())[0], 2)

			a_lower_avg = round(list(results.aggregate(Avg('a_lower')).values())[0], 2)
			a_lower_max = round(list(results.aggregate(Max('a_lower')).values())[0], 2)
			a_lower_min = round(list(results.aggregate(Min('a_lower')).values())[0], 2)
			
			a_crossline_avg = round(list(results.aggregate(Avg('a_crossline')).values())[0], 2)

			
			#Teleop

			t_upper_avg = round(list(results.aggregate(Avg('t_upper')).values())[0], 2)
			t_upper_max = round(list(results.aggregate(Max('t_upper')).values())[0], 2)
			t_upper_min = round(list(results.aggregate(Min('t_upper')).values())[0], 2)

			t_lower_avg = round(list(results.aggregate(Avg('t_lower')).values())[0], 2)
			t_lower_max = round(list(results.aggregate(Max('t_lower')).values())[0], 2)
			t_lower_min = round(list(results.aggregate(Min('t_lower')).values())[0], 2)

			search_run = True
			
			return render(request, 'teamsummary.html', {'results': results, 'results_pit':results_pit, 'search_run':search_run, 'a_upper_avg':a_upper_avg,'a_upper_max':a_upper_max,'a_upper_min':a_upper_min,'a_lower_avg':a_lower_avg,'a_lower_max':a_lower_max,'a_lower_min':a_lower_min,'a_crossline_avg':a_crossline_avg,'t_upper_avg':t_upper_avg,'t_upper_max':t_upper_max,'t_upper_min':t_upper_min,'t_lower_avg':t_lower_avg,'t_lower_max':t_lower_max,'t_lower_min':t_lower_min})
		else:
			search_run = False
			return render(request, 'teamsummary.html', {'search_run':search_run})
