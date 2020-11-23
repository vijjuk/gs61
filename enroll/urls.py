from django.urls import path
from . import views

urlpatterns=[
    path('',views.show_all_img,name='home'),
    path('about/',views.about,name="About"),
    path("profile/",views.User_profile,name="profile"),
    path("changpass/",views.User_change_pass,name="Changepass"),
    path('edit/',views.User_edit,name='edit'),
    path('image/',views.Images,name="images"),
    path('out/',views.Logout,name="lgout"),
    
    path('signup/',views.SignUp,name='Signup'),
    path('login/',views.Login,name="Login"),
    
    
    
    
    
    
    
]