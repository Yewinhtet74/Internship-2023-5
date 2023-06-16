from django.urls import path
from . import views

urlpatterns=[
    path('',views.user,name='user from index'),
    path('register',views.register,name='register from index'),
    path('submit',views.submit,name='submit from index'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.editprofile,name='edit profile')
]