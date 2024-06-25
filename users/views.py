from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.

# views for Login/Logout/register

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return render('profiles')
    
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
           user = User.objects.get(username=username)

        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'Username or password is incorrect')


    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, 'User account was created')
            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, 'An error has occured during registration')
            
        
    context = {'page': page, 'form':form}

    return render(request, 'users/login_register.html', context)

#---------------------------------------------------------------------------------------
# views for Profile
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)
#-------------------------------------------------------------------------------------------

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    projects = profile.project_set.all()
    skills = profile.skill_set.all()
   
    context = {'profile': profile, 'skills': skills, 'projects':projects}
    return render(request, 'users/account.html',context)

#----------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)