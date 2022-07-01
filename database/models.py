from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.FloatField(default = 0)

class Problem(models.Model):
    Problem_ID = models.CharField(max_length=100)
    Problem_name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    difficulty = models.CharField(max_length = 50)
    solved_status = models.CharField(max_length = 10, default = 'Unsolved')
    Score = models.FloatField()

class test_case(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    Input = models.CharField(max_length = 100)
    Output = models.CharField(max_length = 100)

class Submission(models.Model):
    Userp = models.ForeignKey(Users, on_delete = models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    Verdict = models.CharField(max_length=20, default = 'NA')
    Timestamp = models.DateTimeField('submitted at')
    runtime = models.CharField(max_length=2)
