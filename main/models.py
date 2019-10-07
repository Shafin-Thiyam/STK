from django.db import models
from datetime import datetime, date;


class PersonalDetails(models.Model):
    Name = models.CharField(max_length=200)
    Gender = models.CharField(max_length=100)
    Age = models.IntegerField()
    Interest = models.CharField(max_length=200)
    Passport = models.CharField(max_length=200)
    E_Mail = models.CharField(max_length=50)
    Address = models.TextField(default="india")
    DOB = models.DateField( blank=True)
    Linkedin  = models.CharField(max_length=200)
    skype  = models.CharField(max_length=200)
    facebook  = models.CharField(max_length=200)
    git  = models.CharField(max_length=200)
    Primary_contacts = models.CharField(max_length=20)
    Secondary_contacts = models.CharField(max_length=20)
    About_me = models.TextField(default="Developer with diverse Experice")
    Maritial_Status = models.BooleanField(default=True)
    Cv=  models.FileField(upload_to='uploads/CV/', default='upload/CV/CV.pdf')
    def __str__(self):
        return self.Name

class Experience(models.Model):
    Employee_id = models.CharField(max_length=100, primary_key=True)
    Person_ID = models.ForeignKey(PersonalDetails, on_delete=models.DO_NOTHING)
    Company = models.CharField(max_length=200)
    Logo = models.ImageField(upload_to='companyLogo/', blank=True)
    Designation = models.CharField(max_length=100, default="Software Engineer")
    Location = models.CharField(max_length=100, default="India")
    From = models.DateField(default=date.today)
    To = models.DateField(blank=True,null=True)
    NoticePeriod = models.IntegerField()
    ServingNotice = models.BooleanField(default=False)
    startOfNotice = models.DateField(blank=True,null=True)
    endOfNotice = models.DateField(blank=True,null=True)
    

    def __str__(self):
        return self.Employee_id

class Academic(models.Model):
    College = models.CharField(max_length=200)
    Course = models.CharField(max_length=200)
    Specialization = models.CharField(max_length=200)
    Location = models.CharField(max_length=200, default="Mumbai, India")
    From = models.DateField( blank=True)
    To = models.DateField(default=date.today, blank=True,null=True)
    def __str__(self):
        return self.Course+" specialization in "+self.Specialization

class Skillsets(models.Model):
    Skill = models.CharField(max_length=200)
    Proficiency_Percentage  = models.IntegerField()
    def __str__(self):
        return self.Skill

class contact(models.Model):
    Name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, default='')
    message = models.TextField(blank=True, default='')
    Contact_date = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.Name

