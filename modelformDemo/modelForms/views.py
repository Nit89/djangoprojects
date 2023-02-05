from django.shortcuts import render
from modelForms.forms import ProjectForm
from modelForms.models import Project

# Create your views here.

def index(request):
    return render(request,'index.html')

def listProjects(request):
    projectList = Project.objects.all()
    return render(request,'listproject.html',{'projects':projectList})

def addProject(request):
    form = ProjectForm()
    if request.method=='POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    
    return render(request,'addproject.html',{'form':form})
    
