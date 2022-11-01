from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

def author(request):
    if request.session.has_key('user_loged'):
        return render(request,'blog/pages/about author.html')

    else:
        return render(request,'blog/pages/about author.html')

def login(request):
    if request.session.has_key('user_loged'):
        return redirect('home')
    else:
        return render(request,'blog/pages/login.html')

def home(request):
    if request.session.has_key('user_loged'):
        fetch_Blog = Blog.objects.order_by("-post_date")
        return render(request,'blog/pages/home.html',{'Blog_post':fetch_Blog})
    elif request.POST:
        username=request.POST['username']
        password= request.POST['password']
        userlogin=Blog_User.objects.filter(username=username,password=password).count()
        if userlogin > 0:
            request.session['user_loged']=True
            request.session['userid']=Blog_User.objects.values('id').filter(username=username,password=password)[0]['id']
            fetch_Blog=Blog.objects.all()
            return render(request,'blog/pages/home.html',{'Blog_post':fetch_Blog})
        else:
            messages.error(request,'Invalid user name or password')
            return redirect('login')
    else:
        messages.error(request,'You have to login first')
        return redirect('login')

    #return HttpResponse("<h1> You'r Log IN </h1>")


def logout(request):
    if request.session.has_key('user_loged'):
        del request.session['user_loged']
        return redirect('login')
    else:
        messages.error(request,'No user is login')
        return redirect('login')

def register(request):
    if request.POST:
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']

        registration= Blog_User(username=username,email=email,password=password)
        registration.save()
        return redirect('login')
    else:
        return register(request)
    #return HttpResponse("<h1> You'r Log Out </h1>")

def createpost(request):
    if request.session.has_key('user_loged'):
        if request.POST:
            name=request.POST['good_name']
            post_tittle=request.POST['title']
            post=request.POST['post']
            img_upload=request.FILES['image']
            #post_date=request.POST['post_date']
            user_id=request.session['userid']
            blog=Blog(good_name=name,tittle=post_tittle,post=post,image=img_upload)
            blog.user_id_id=user_id
            blog.save()
            return redirect('home')
        else:
            return render(request,'blog/pages/createpost.html')
    else:
        messages.error(request,"you have to login first")
        return redirect('login')


def read_more(request,id):
    #return HttpResponse(str(id))
    if request.POST:
        Comnt=request.POST['comment']
        user_id=request.session['userid']
        post_id=id
        Cmnt=Comment(comments=Comnt)
        Cmnt.post_id_id=post_id
        Cmnt.user_id_id=user_id
        Cmnt.save()
        #return HttpResponse("save--------------------")
    fetch_Blog = Blog.objects.all().filter(id=id)
    cmnt=Comment.objects.order_by("-cmnt_date").filter(post_id=id)
    #user=Blog_User.objects.all().filter()
    return render(request,'blog/pages/readmore.html',{'Blog_post':fetch_Blog,"comment":cmnt})
def signup(request):
    return render(request,'blog/pages/signup.html')
# Create your views here.
