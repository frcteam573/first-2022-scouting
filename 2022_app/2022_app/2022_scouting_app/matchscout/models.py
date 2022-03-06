from django.db import models

# Create your models here.
class matchscout(models.Model):
	# pre-match info
	name = models.CharField(max_length = 50)

	team_num = models.IntegerField()

	match_num = models.IntegerField()

	alliance_colors = (('Red','Red'),('Blue','Blue'))
	alliance = models.CharField(max_length = 4, choices = alliance_colors, default = 'Red')

	starting_position = ((1, 'Zone 1'), (2, 'Zone 2'), (3, 'Zone 3'), (4, 'Zone 4'))
	starting = models.IntegerField(choices = starting_position, default = 'Zone 1')

	a_lower = models.IntegerField(default = 0)
	a_upper = models.IntegerField(default = 0)

	yesno = ((0, 'No'),(1, 'Yes'))
	yesno2 = ((0, 'No'),(1, 'Yes'))
	a_crossline = models.IntegerField(choices = yesno, default = 0)

	a_human = models.IntegerField(choices = yesno2, default = 0)

	t_lower = models.IntegerField(default = 0)
	t_upper = models.IntegerField(default = 0)

	ending_location = ((1, 'Floor'), (2, 'Low Rung'), (3, 'Middle Rung'),(4, 'High Rung'), (5, 'Traversal Rung'))
	t_ending = models.IntegerField(choices = ending_location, default = 1)

	comments = models.TextField()