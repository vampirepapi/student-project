from django.db import models

# Create your models here.
class StudentDetails(models.Model):
	student_id = models.AutoField(primary_key=True)
	student_name = models.CharField(max_length=50)
	student_class = models.CharField(max_length=50)