from django.urls import path
from .views import profiles, userProfile, loginUser, logoutUser

urlpatterns = [
    #-------------------------------------------
    #path for login/logout function

    path("login/", loginUser, name="login"),
    path("logout/", logoutUser, name="logout"),

    #-----------------------------------------

    path('', profiles, name="profiles"),
    path('profile/<str:pk>/',userProfile, name="user-profile")
    
]
