from django.urls import include, path
from . import views

app_name = 'students'
urlpatterns = [
    path('insertStudent/', views.insertStudent.as_view()),
    path('listStudent/', views.listStudent.as_view()),
    path('deleteStudent/', views.deleteStudent.as_view()),
    
    ]