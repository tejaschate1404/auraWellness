
from django.urls import path 
from . import views
urlpatterns = [
   
    path('', views.indexAdmin, name='indexAdmin'),
    path('base/', views.baseAdmin, name='baseAdmin'),
    
    # Counceiling
    path('add-counceling/', views.addCounseling, name='addCounseling'),
    path('add-category/', views.addCategory, name='addCategory'),
    path('view-counceling/', views.viewCounseling, name='viewCounseling'),
    path('delete/<int:record_id>/', views.delete_counseling, name='delete_counseling'),
    path('view-counseling/<int:record_id>/', views.view_counseling_details, name='view_counseling_details'),
    

    # Physical Healing
     # path('add-counseling-physical/', views.addPhysicalHealing, name='addCounselingPhysical'),
     path('add-category-physical/', views.addCategoryPhysical, name='addCategoryPhysical'),
    # path('view-counseling-physical/', views.viewCounseling, name='viewCounselingPhysical'),
    # path('delete-counseling/<int:record_id>/', views.delete_counseling, name='deleteCounseling'),
    # path('view-counseling-physical/<int:record_id>/', views.view_counseling_details, name='viewCounselingDetails'),

    #Auth
    path('signup/',views.signup_view , name="signupAdmin"),
    path('login/',views.login_view , name="loginAdmin"),
    path('logout/',views.logout_view , name="logoutAdmin"),

]
