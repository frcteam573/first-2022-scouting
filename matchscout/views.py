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
		
			#Sandstorm
			s_hatches_1_avg = round(list(results.aggregate(Avg('s_hatches_1')).values())[0], 2)
			s_hatches_1_max = round(list(results.aggregate(Max('s_hatches_1')).values())[0], 2)
			s_hatches_1_min = round(list(results.aggregate(Min('s_hatches_1')).values())[0], 2)

			s_cargo_1_avg = round(list(results.aggregate(Avg('s_cargo_1')).values())[0], 2)
			s_cargo_1_max = round(list(results.aggregate(Max('s_cargo_1')).values())[0], 2)
			s_cargo_1_min = round(list(results.aggregate(Min('s_cargo_1')).values())[0], 2)

			s_hatches_2_avg = round(list(results.aggregate(Avg('s_hatches_2')).values())[0], 2)
			s_hatches_2_max = round(list(results.aggregate(Max('s_hatches_2')).values())[0], 2)
			s_hatches_2_min = round(list(results.aggregate(Min('s_hatches_2')).values())[0], 2)

			s_cargo_2_avg = round(list(results.aggregate(Avg('s_cargo_2')).values())[0], 2)
			s_cargo_2_max = round(list(results.aggregate(Max('s_cargo_2')).values())[0], 2)
			s_cargo_2_min = round(list(results.aggregate(Min('s_cargo_2')).values())[0], 2)

			s_hatches_3_avg = round(list(results.aggregate(Avg('s_hatches_3')).values())[0], 2)
			s_hatches_3_max = round(list(results.aggregate(Max('s_hatches_3')).values())[0], 2)
			s_hatches_3_min = round(list(results.aggregate(Min('s_hatches_3')).values())[0], 2)

			s_cargo_3_avg = round(list(results.aggregate(Avg('s_cargo_3')).values())[0], 2)
			s_cargo_3_max = round(list(results.aggregate(Max('s_cargo_3')).values())[0], 2)
			s_cargo_3_min = round(list(results.aggregate(Min('s_cargo_3')).values())[0], 2)

			
			

			#Teleop
			t_hatches_1_avg = round(list(results.aggregate(Avg('t_hatches_1')).values())[0], 2)
			t_hatches_1_max = round(list(results.aggregate(Max('t_hatches_1')).values())[0], 2)
			t_hatches_1_min = round(list(results.aggregate(Min('t_hatches_1')).values())[0], 2)

			t_cargo_1_avg = round(list(results.aggregate(Avg('t_cargo_1')).values())[0], 2)
			t_cargo_1_max = round(list(results.aggregate(Max('t_cargo_1')).values())[0], 2)
			t_cargo_1_min = round(list(results.aggregate(Min('t_cargo_1')).values())[0], 2)

			t_hatches_2_avg = round(list(results.aggregate(Avg('t_hatches_2')).values())[0], 2)
			t_hatches_2_max = round(list(results.aggregate(Max('t_hatches_2')).values())[0], 2)
			t_hatches_2_min = round(list(results.aggregate(Min('t_hatches_2')).values())[0], 2)

			t_cargo_2_avg = round(list(results.aggregate(Avg('t_cargo_2')).values())[0], 2)
			t_cargo_2_max = round(list(results.aggregate(Max('t_cargo_2')).values())[0], 2)
			t_cargo_2_min = round(list(results.aggregate(Min('t_cargo_2')).values())[0], 2)

			t_hatches_3_avg = round(list(results.aggregate(Avg('t_hatches_3')).values())[0], 2)
			t_hatches_3_max = round(list(results.aggregate(Max('t_hatches_3')).values())[0], 2)
			t_hatches_3_min = round(list(results.aggregate(Min('t_hatches_3')).values())[0], 2)

			t_cargo_3_avg = round(list(results.aggregate(Avg('t_cargo_3')).values())[0], 2)
			t_cargo_3_max = round(list(results.aggregate(Max('t_cargo_3')).values())[0], 2)
			t_cargo_3_min = round(list(results.aggregate(Min('t_cargo_3')).values())[0], 2)
			
		
		
		

		

			level_1 = round(results.filter(ending=1).count()/results.count() * 100, 2)
			level_2 = round(results.filter(ending=2).count()/results.count() * 100, 2)
			level_3 = round(results.filter(ending=3).count()/results.count() * 100, 2)


			search_run = True
			return render(request, 'teamsummary.html', {'results': results, 'results_pit':results_pit, 'search_run':search_run, 's_hatches_1_avg':s_hatches_1_avg, 's_hatches_1_max':s_hatches_2_max,'s_hatches_1_min':s_hatches_1_min, 's_cargo_1_avg':s_cargo_1_avg, 's_cargo_1_max':s_cargo_1_max, 's_cargo_1_min':s_cargo_1_min, 's_hatches_2_avg':s_hatches_2_avg, 's_hatches_2_max':s_hatches_2_max, 's_hatches_2_min':s_hatches_2_min, 's_cargo_2_avg':s_cargo_2_avg, 's_cargo_2_max':s_cargo_2_max, 's_cargo_2_min':s_cargo_2_min, 's_hatches_3_avg':s_hatches_3_avg, 's_hatches_3_max':s_hatches_3_max, 's_hatches_3_min':s_hatches_3_min, 's_cargo_3_avg':s_cargo_3_avg, 's_cargo_3_max':s_cargo_3_max, 's_cargo_3_min':s_cargo_3_min, 't_hatches_1_avg':t_hatches_1_avg, 't_hatches_1_max':t_hatches_1_max, 't_hatches_1_min':t_hatches_1_min, 't_cargo_1_avg':t_cargo_1_avg, 't_cargo_1_max':t_cargo_1_max, 't_cargo_1_min':t_cargo_1_min, 't_hatches_2_avg':t_hatches_2_avg, 't_hatches_2_max':t_hatches_2_max, 't_hatches_2_min':t_hatches_2_min, 't_cargo_2_avg':t_cargo_2_avg, 't_cargo_2_max':t_cargo_2_max, 't_cargo_2_min':t_cargo_2_min, 't_hatches_3_avg':t_hatches_3_avg, 't_hatches_3_max':t_hatches_3_max, 't_hatches_3_min':t_hatches_3_min, 't_cargo_3_avg':t_cargo_3_avg, 't_cargo_3_max':t_cargo_3_max, 't_cargo_3_min':t_cargo_3_min, 'level_1':level_1, 'level_2':level_2, 'level_3':level_3})
		else:
			search_run = False
			return render(request, 'teamsummary.html', {'search_run':search_run})
	else:
		search_run = False
		return render(request, 'teamsummary.html', {'search_run':search_run}) 
