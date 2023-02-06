from django.shortcuts import redirect, render
from fbvApp.models import Student
from fbvApp.forms import StudentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def getStudents(request):
    Students = Student.objects.all()
    return render(request,'index.html',{'students':Students})

@login_required
def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'create.html',{'form':form})

@login_required
def deleteStudent(request,id):
    student =Student.objects.get(id=id)
    student.delete()
    return redirect('/')


@login_required
def updateStudent(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method=='POST':
        form = StudentForm(request.POST,instance =student)
        if form.is_valid(): 
            form.save()
            return redirect('/')
    return render(request,'update.html',{'form':form})
     
    
  