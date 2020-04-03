from .views import (index,signin,newRequest,logIn,viewBox,fonts,search,tf,softwears,about_us)
from django.urls import path,include


urlpatterns = [
    path('',index),
    path('signin',signin),
    path('requestLink',newRequest),
    path('login',logIn),
    path('view',viewBox),
    path('fonts',fonts),
    path('search',search),
    path('tf',tf),
    path("sw",softwears),
    path("about_us",about_us)

]
