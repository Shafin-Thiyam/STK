from django.contrib import admin
from .models import Projects 
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display=('proj_id','Title','Employee_id','Git_repo','description','Skill_used')
    list_display_links=('proj_id','Title',)
    list_per_page=10

admin.site.register(Projects, ProjectsAdmin)