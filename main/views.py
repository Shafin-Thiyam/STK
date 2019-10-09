from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from . models import Academic, Experience, contact, PersonalDetails, Skillsets
from projects.models import Projects
import sendgrid
import os
from datetime import date
from sendgrid.helpers.mail import *


def index(request):
    if request.method == 'POST':
        recruiterName= request.POST['name']
        recruiterEmail= request.POST['email']        
        msgSub= request.POST['subject']
        msg= request.POST['message']
        contacted=contact(Name=recruiterName, email=recruiterEmail,subject=msgSub,message=msg)
        contacted.save()

        message = Mail(from_email=os.environ.get('SENDGRDMAIL'), 
			   to_emails=[recruiterEmail,os.environ.get('CCMAIL'),],
			   subject='Re:'+msgSub,
			   plain_text_content='Thanks '+recruiterName+' for contacting me. Looking forward to discuss further about the position if my profile suite your requirement',
			   html_content='<p>Thanks '+recruiterName+' for contacting me.</p><p>Looking forward to discuss further about the position if my profile suite your requirement</p>')

        #message = Mail(from_email=os.environ.get('CCMAIL'), to_emails=recruiterEmail, subject='Re:'+msgSub, html_content='<p>Thanks '+recruiterName+' for contacting me.</p><p>Looking forward to discuss further about the position if my profile suite your requirement</p>')
        try:
            sg =sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRIDMAILKEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(str(e))
        # send_mail('Re:'+msgSub,'Thanks '+recruiterName+', for contacting me.'+"\n"+'Looking forward to discuss further about the position if my profile suite your requirement', os.environ.get('CCMAIL'),[recruiterEmail,os.environ.get('CCMAIL')], fail_silently=True)
        messages.success(request,'Really Thankfull for contacting me')
        return redirect('/')
    else:
        AcademicsDetails=Academic.objects.all().order_by('-From')
        ExperienceDetails=Experience.objects.all().order_by('-From')
        Recent_Desg=Experience.objects.all().order_by('-From')[0:1]
        Personal=PersonalDetails.objects.all()
        SkillsetDetails=Skillsets.objects.all().order_by('-Proficiency_Percentage')
        Experience.objects.filter(ServingNotice=True, endOfNotice=str(date.today())).update(ServingNotice=False, To=date.today(), endOfNotice=None, startOfNotice=None)
        
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
