from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('view/<int:id>/',views.user_detail),
    path('view/',views.user_list),
    path('editdata/',views.edit_user)
]