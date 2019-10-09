from django.shortcuts import render
from django.http import HttpResponse
from . models import Projects
from main.models import Experience, PersonalDetails
# Create your views here.
def project(request, Employee_id):
    PrjDetails=Projects.objects.filter(Employee_id=Employee_id)
    # Recent_Desg=Experience.objects.all().order_by('-From')[0:1]
    Recent_Desg=(Experience.objects.all().filter(visible=True).order_by('-From')[0:1])[0].Designation
    # ExperienceDetails=Experience.objects.all().order_by('-From')
    ExperienceDetails=Experience.objects.all().filter(visible=True).order_by('-From')
    eid=Projects.objects.filter(Employee_id=Employee_id)[0:1]
    Personal=PersonalDetails.objects.all()
    #PrjDetails=Projects.objects.all()
    proj_data={
        'project' : PrjDetails,
        'personal' : Personal,
        'Experience' : ExperienceDetails,
        'Recent': Recent_Desg,
        'empID' : eid,
    }
    return render(request,'projects/project.html',proj_data)
