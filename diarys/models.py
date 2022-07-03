from django.db import models

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    modelkey = models.CharField(max_length=10)
    
class Routine_detail(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    weight = models.FloatField()
    reps = models.IntegerField()
    
class Routine_comment(models.Model):
    comment = models.TextField()
    modelkey = models.CharField(max_length=10)