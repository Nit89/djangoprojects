from django.shortcuts import redirect, render
from fbvApp.models import Student
from fbvApp.forms import StudentForm
# Create your views here.

def getStudents(request):
    Students = Student.objects.all()
    return render(request,'index.html',{'students':Students})


def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'create.html',{'form':form})

def deleteStudent(request,id):
    student =Student.objects.get(id=id)
    student.delete()
    return redirect('/')

def updateStudent(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method=='POST':
        form = StudentForm(request.POST,instance =student)
        if form.is_valid(): 
            form.save()
            return redirect('/')
    return render(request,'update.html',{'form':form})
     
    
  