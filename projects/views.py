from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project, Review, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# projects view
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html',context)

#single project view
def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html',{'project': projectObj})

@login_required(login_url="login")
def create_Project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        # print(request.POST)
    context = {'form':form}
    
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    # project = Project.objects.get(id=pk)
    project = get_object_or_404(Project, id=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm(instance=project)    
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    project = get_object_or_404(Project, id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context= {'object':project}
    
    return render(request, 'projects/delete_template.html', context)
        
        

