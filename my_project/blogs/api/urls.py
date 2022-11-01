from django.urls import path
from blogs.api import views


blog='blog_api'
urlpatterns=[
    path('<int:id>/',views.get_api_view,name='blog_api')
]