from django.urls import path
from .views import electro 

app_name = "electro_project"
urlpatterns = [
    path('project_1/', electro,  name='electro'),
    
]

