from django.db import models

# Create your models here.
class pitscout(models.Model):

	team_num = models.IntegerField(unique = True)

	drivetrain_types = (('4-wheel tank','4-wheel tank'), ('6-wheel tank','6-wheel tank'),('Swerve','Swerve'),('Omni','Omni'),('Mechanim','Mechanim'),('Other','Other'))
	drivetrain = models.CharField(max_length = 20, choices = drivetrain_types, default = 'Other')

	start_location_ls = (('Zone 1','Zone 1'),('Zone 2','Zone 2'), ('Zone 3', 'Zone 3'), ('Zone 4', 'Zone 4'), ('Zone 5', 'Zone 5'))
	start_location = models.CharField(max_length = 6, choices = start_location_ls, default = 'Zone 1')

	yesno = ((1, 'Yes'), (0, 'No'))

	a_crossline = models.IntegerField(choices = yesno, default = 0)

	a_goal_ls = (('upper', 'upper'), ('lower', 'lower'))
	a_goal = models.CharField(max_length = 5, choices = a_goal_ls, default = 'upper')

	a_ballscore =  models.IntegerField(default = 0)

#goals

	t_lowergoal = models.IntegerField(choices = yesno, default = 0)
	t_uppergoal = models.IntegerField(choices = yesno, default = 0)

#ball intake 

	t_humanplayer = models.IntegerField(choices = yesno, default = 0)
	t_ground = models.IntegerField(choices = yesno, default = 0)
	strength = models.TextField()

	comments = models.TextField()

	name = models.CharField(max_length = 50)

	#robot_photo = models.FileField(upload_to='robot_photo/',max_length=1000,default='')
