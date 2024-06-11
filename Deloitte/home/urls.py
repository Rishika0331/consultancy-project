from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage),
    path('index.html/',views.homepage),
    path('consultancy-project/about.html/',views.aboutus),
    path('consultancy-project/services.html/',views.services),
    path('consultancy-project/career.html/',views.career),
    path('consultancy-project/signup.html/',views.signup),
    path('consultancy-project/login.html/',views.login),
    path('consultancy-project/contact.html/',views.contactus),
    
    
]