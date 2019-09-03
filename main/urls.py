from django.urls import path
from . import views
from projects import views as pr_v

urlpatterns=[
        path('', views.index, name='index'),
        path('<str:Employee_id>', pr_v.project, name='project'),
]
