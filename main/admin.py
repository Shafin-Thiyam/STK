from django.contrib import admin
from .models import PersonalDetails, Experience, Academic, Skillsets, contact 
# Register your models here.
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display=('id','Name','Age','E_Mail','Primary_contacts','Passport')
    list_display_links=('id','Name',)
    list_per_page=10

class ExperienceAdmin(admin.ModelAdmin):
    list_display=('Employee_id','Company','From','To')
    list_display_links=('Employee_id','Company',)
    list_filter=('From',)
    list_per_page=10

class AcademicAdmin(admin.ModelAdmin):
    list_display=('id','College','Course','Specialization')
    list_display_links=('id','College',)
    list_per_page=10

class SkillsetsAdmin(admin.ModelAdmin):
    list_display=('id','Skill')
    list_per_page=10

class ContactAdmin(admin.ModelAdmin):
    list_display=('Name','email','subject','Contact_date')
    list_display_links=('Name',)
    list_filter=('Contact_date',)
    list_per_page=10


admin.site.register(PersonalDetails, PersonalDetailsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Academic, AcademicAdmin)
admin.site.register(Skillsets, SkillsetsAdmin)
admin.site.register(contact,ContactAdmin)
