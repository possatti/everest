from django.db import models

class Skill(models.Model):
	name = models.CharField(max_length=30, unique=True)
	path = models.CharField(max_length=150)
	tree_level = models.IntegerField()
	icon = models.ImageField()

class Question(models.Model):
	DIFFICULTY_CHOICES = (('E','EASY'), ('M','MEDIUM'), ('H', 'HARD'))
	name = models.CharField(max_length=50)
	points = models.IntegerField()
	difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES)
	skill = models.ForeignKey('core.Skill', models.CASCADE)

class Student(models.Model):
	user = models.OneToOneField('auth.User', models.CASCADE)
	points = models.IntegerField()

class Solution(models.Model):
	STATUS_CHOICES = [('P', 'Pending'), ('Q', 'In Queue'), ('C', 'Correct'), ('I', 'Incorrect'), ('T', 'TLE')]
	code = models.TextField() # Or maybe FileField?
	submission_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	user = models.ForeignKey('core.Student', models.CASCADE)
	question = models.ForeignKey('core.Question', models.CASCADE)
