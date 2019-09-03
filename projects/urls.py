from django.urls import path
from . import views

urlpatterns=[
        path('<str:Employee_id>', views.project, name='projects'),
]
