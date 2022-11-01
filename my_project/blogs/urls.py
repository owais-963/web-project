from django.urls import path
from .import views

urlpatterns =[
    path('',views.author,name='author'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('registeration',views.register,name='register'),
    path('signup',views.signup,name='signup'),
    path('createpost',views.createpost,name='create'),
    path('readmore/<int:id>',views.read_more,name='read_more')
]