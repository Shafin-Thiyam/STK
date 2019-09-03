from django.db import models
from datetime import datetime, date;
from main.models import Experience

class Projects(models.Model):
    proj_id = models.CharField(max_length=100, primary_key=True)
    Employee_id = models.ForeignKey(Experience, on_delete=models.DO_NOTHING)
    Git_repo = models.CharField(max_length=200, blank=True, default='copyright') 
    Title =  models.CharField(max_length=200)
    description = models.TextField()
    Skill_used =  models.CharField(max_length=100, default='xsl') 
    def __str__(self):
        return self.Title
