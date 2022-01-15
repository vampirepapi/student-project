from ..models import *
import sys,inspect

def insertStudent(self,request,format=None):
	try:        
	    student = StudentDetails.objects.get(student_name=request['student_name'])
	except:
	    student = StudentDetails.objects.create(student_name=request['student_name'])
	    student.student_class=request['student_class']
	    student.save()
	    print(student)


def listStudent(self,request,format=None):
	data=[]
	students= StudentDetails.objects.all().order_by('student_name')
	for student in students:
		data.append({"student_id":student.student_id,"student_name":student.student_name,"student_class":student.student_class})
	return data


def deleteStudent(self,request,format=None):
	student = StudentDetails.objects.get(student_id=request['student_id'])
	print(student)
	student.delete()

