from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from . models import Academic, Experience, contact, PersonalDetails, Skillsets
from projects.models import Projects


def index(request):
    if request.method == 'POST':
        recruiterName= request.POST['name']
        recruiterEmail= request.POST['email']        
        msgSub= request.POST['subject']
        msg= request.POST['message']
        contacted=contact(Name=recruiterName, email=recruiterEmail,subject=msgSub,message=msg)
        contacted.save()
        send_mail('Re:'+msgSub,'Thanks '+recruiterName+', for contacting me.'+"\n"+'Looking forward to discuss further about the position if my profile suite your requirement', 'thiyam.shafin@gmail.com',[recruiterEmail,'shafin.thiyam@outlook.com'], fail_silently=False)
        messages.success(request,'Really Thankfull for contacting me')
        return redirect('/')
    else:
        AcademicsDetails=Academic.objects.all().order_by('-From')
        ExperienceDetails=Experience.objects.all().order_by('-From')
        Recent_Desg=Experience.objects.all().order_by('-From')[0:1]
        Personal=PersonalDetails.objects.all()
        SkillsetDetails=Skillsets.objects.all().order_by('-Proficiency_Percentage')
        profile_data={
            'personal' : Personal,
            'academic' : AcademicsDetails,
            'Experience' : ExperienceDetails,
            'Skillsets': SkillsetDetails,
            'Recent': Recent_Desg,
        }    
        return render(request,'main/index.html',profile_data)

def project(request):
    return render(request,'main/project.html')
