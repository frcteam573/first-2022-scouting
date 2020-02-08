from django.db import models

# Create your models here.
class pitscout(models.Model):

	team_num = models.IntegerField(unique = True)

	drivetrain_types = (('4-wheel tank','4-wheel tank'), ('6-wheel tank','6-wheel tank'),('Swerve','Swerve'),('Omni','Omni'),('Mechanim','Mechanim'),('Other','Other'))
	drivetrain = models.CharField(max_length = 20, choices = drivetrain_types, default = 'Other')

	platform_start_yn = (('yes','yes'),('no','no'))
	platform_start = models.CharField(max_length = 5, choices = platform_start_yn, default = 'yes')

	platform_end_level = (('1','Level 1'),('2','Level 2'),('3','Level 3'),('0', 'None'))
	platform_end = models.CharField(max_length = 10, choices = platform_end_level, default = 'None')

	climb_time = models.IntegerField()

	disk_options = (('Ground','Ground'),('Human Player','Human Player'),('None','None'),('Both','Both'))
	disk = models.CharField(max_length = 20, choices = disk_options, default = 'None')

	ball_options = (('Ground','Ground'),('Human Player','Human Player'),('None','None'),('Both','Both'))
	ball = models.CharField(max_length = 20, choices = ball_options, default = 'None')

	auton_yn = (('yes','yes'),('no','no'))
	auton = models.CharField(max_length = 5, choices = auton_yn, default = 'yes')

	camerafeed_yn = (('yes','yes'),('no','no'))
	camerafeed = models.CharField(max_length = 5, choices = camerafeed_yn, default = 'yes')

	above_ground_yn = (('yes','yes'),('no','no')) 
	above_ground = models.CharField(max_length = 5, choices = above_ground_yn, default = 'yes')

	scoring_priority = models.CharField(max_length = 100)

	strength = models.TextField()

	comments = models.TextField()

	name = models.CharField(max_length = 50)

	#robot_photo = models.FileField(upload_to='robot_photo/',max_length=1000,default='')
