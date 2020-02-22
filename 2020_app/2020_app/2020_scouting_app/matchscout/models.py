from django.db import models

# Create your models here.
class matchscout(models.Model):
	# pre-match info
	name = models.CharField(max_length = 50)

	team_num = models.IntegerField()

	match_num = models.IntegerField()

	alliance_colors = (('Red','Red'),('Blue','Blue'))
	alliance = models.CharField(max_length = 4, choices = alliance_colors, default = 'Red')

	starting_position = ((1, 'Zone 1'), (2, 'Zone 2'), (3, 'Zone 3'), (4, 'Zone 4'), (5, 'Zone 5'))
	starting = models.IntegerField(choices = starting_position, default = 'Zone 1')

	#starting_piece = (('Hatch','Hatch'),('Cargo','Cargo'))
	#start_piece = models.CharField(max_length = 10, choices = starting_piece, default = 'Hatch')
	# during match info

	a_lower = models.IntegerField(default = 0)
	a_upper = models.IntegerField(default = 0)
	a_inner = models.IntegerField(default = 0)
	yesno = ((0, 'No'),(1, 'Yes'))
	a_crossline = models.IntegerField(choices = yesno, default = 'No')


	t_lower = models.IntegerField(default = 0)
	t_upper = models.IntegerField(default = 0)
	t_inner = models.IntegerField(default = 0)
	yesno2 = ((0, 'No'),(1, 'Yes'))
	yesno3 = ((0, 'No'),(1, 'Yes'))
	positioncontrol = models.IntegerField(choices = yesno2, default = 'No')
	rotationcontrol= models.IntegerField(choices = yesno3, default = 'No')
	#s_hatches_sum = models.(s_hatches_1 + s_hatches_2 + s_hatches_3)


	# post-match info
	yesno4 = ((0, 'No'),(1, 'Yes'))
	yesno5 = ((0, 'No'),(1, 'Yes'))
	yesno6 = ((0, 'No'),(1, 'Yes'))
	ending_climb = models.IntegerField(choices = yesno4, default = 'No') 
	ending_level = models.IntegerField(choices = yesno5, default = 'No')
	ending_buddy = models.IntegerField(choices = yesno6, default = 'No')
	

	#score = models.IntegerField(blank = True)

	comments = models.TextField()