from django.db import models

# Create your models here.
class matchscout(models.Model):
	# pre-match info
	name = models.CharField(max_length = 50)

	team_num = models.IntegerField()

	match_num = models.IntegerField()

	alliance_colors = (('Red','Red'),('Blue','Blue'))
	alliance = models.CharField(max_length = 4, choices = alliance_colors, default = 'Red')

	starting_level = ((1, 'Level 1'), (2, 'Level 2'))
	starting = models.IntegerField(choices = starting_level, default = 'Level 1')

	starting_piece = (('Hatch','Hatch'),('Cargo','Cargo'))
	start_piece = models.CharField(max_length = 10, choices = starting_piece, default = 'Hatch')
	# during match info

	s_hatches_1 = models.IntegerField(default = 0)
	s_hatches_2 = models.IntegerField(default = 0)
	s_hatches_3 = models.IntegerField(default = 0)

	s_cargo_1 = models.IntegerField(default = 0)
	s_cargo_2 = models.IntegerField(default = 0)
	s_cargo_3 = models.IntegerField(default = 0)	

	t_hatches_1 = models.IntegerField(default = 0)
	t_hatches_2 = models.IntegerField(default = 0)
	t_hatches_3 = models.IntegerField(default = 0)

	t_cargo_1 = models.IntegerField(default = 0)
	t_cargo_2 = models.IntegerField(default = 0)
	t_cargo_3 = models.IntegerField(default = 0)

	#s_hatches_sum = models.(s_hatches_1 + s_hatches_2 + s_hatches_3)


	# post-match info
	ending_level = ((0, 'None'), (1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'))
	ending = models.IntegerField(choices = ending_level, default = 'None')

	

	#score = models.IntegerField(blank = True)

	comments = models.TextField()