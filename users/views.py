from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.

# views for Login/Logout

def loginUser(request):
    if request.user.is_authenticated:
        return render('profiles')
    
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
           user = User.objects.get(username=username)

        except:
            print('Username doesnot exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username or password is incorrect')


    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

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