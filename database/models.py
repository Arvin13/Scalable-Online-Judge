from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.FloatField(default = 0)

class Contest(models.Model):
        con_id = "Contest 1"
        Contest_ID = models.CharField(max_length=100, default = con_id)
        Contest_name = models.CharField(max_length=100, default = con_id)
        def __str__(self):
            return self.Contest_name

class Problem(models.Model):
    contest = models.ForeignKey(Contest, on_delete = models.CASCADE)
    Problem_ID = models.CharField(max_length=100)
    Problem_name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    difficulty = models.CharField(max_length = 50)
    solved_status = models.CharField(max_length = 10, default = 'Unsolved')
    Score = models.FloatField()
    def __str__(self):
        return self.Problem_name

class test_case(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    Input = models.CharField(max_length = 100)
    Output = models.CharField(max_length = 100)
    def __str__(self):
        io = "Input:  %s    "%self.Input + "||    Outputi:  %s"%self.Output
        return io

class Submission(models.Model):
    Userp = models.ForeignKey(Users, on_delete = models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    Verdict = models.CharField(max_length=20, default = 'NA')
    Timestamp = models.DateTimeField('submitted at')
    runtime = models.CharField(max_length=2)
