
from django.urls import path 
from . import views
urlpatterns = [
   
    path('', views.indexAdmin, name='indexAdmin'),
    path('base/', views.baseAdmin, name='baseAdmin'),
    
    # Counceiling
    path('add-counceling/', views.addCounseling, name='addCounseling'),
    path('add-category/', views.addCategory, name='addCategory'),
    path('view-counceling/', views.viewCounseling, name='viewCounseling'),


    #Auth
    path('signup/',views.signup_view , name="signupAdmin"),
    path('login/',views.login_view , name="loginAdmin"),
    path('logout/',views.logout_view , name="logoutAdmin"),

]
