from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,request,JsonResponse,response
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
import json
from django.core.serializers import serialize
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .forms import UserRegistrationForm



# Create your views here.


def about(request):
    return render(request,'blogs/about.html')

def home(request):
    return render(request, 'blogs/home.html')


def LinkedIn(request):
    return HttpResponseRedirect('https://www.linkedin.com/in/praharsha-sarma')

def GitHub(request):
    return HttpResponseRedirect('https://github.com/praharsha05')



def delete_publish(request,id):
    del_id = id
    obj = get_object_or_404(models.blogs, id=del_id)
    if request.method == 'POST':
        obj.delete()
    return redirect('index')

def save_draft(request):
    print(request)
    return redirect('drafts')


def delete_draft(request,id):
    del_id = id
    obj = get_object_or_404(models.drafts, id=del_id)
    if request.method == 'POST':
        obj.delete()
    return redirect('drafts')

def publish_draft(request,id):
    del_id = id
    obj = get_object_or_404(models.drafts, id=del_id)
    if request.method == 'POST':
        form = models.blogs()
        form.title = obj.title
        form.category = obj.category
        form.text = obj.text
        form.uname = obj.uname
        form.save()
    obj.delete()
    return redirect('drafts')

def update_draft(request,id):
    edit_id = id
    obj = get_object_or_404(models.drafts, id=edit_id)
    if request.method=='POST':
        obj.title = request.POST.get('title')
        obj.category = request.POST.get('category')
        obj.text = request.POST.get('text')
        obj.save()
        return redirect('drafts')
    else:
        response = {
            "draft" : obj,
            "id" : edit_id
        }
        return render(request, 'blogs/edit.html',context=response)



def edit_publish(request,id):
    edit_id = id
    obj = get_object_or_404(models.blogs, id=edit_id)
    if request.method == 'POST':
        form = models.drafts()
        form.title = obj.title
        form.category = obj.category
        form.text = obj.text
        form.uname = obj.uname
        form.date = obj.date
        form.save()
    obj.delete()
    return redirect('drafts')

def icon_publish(request,id,icon):
    req_id = id
    icon_type = icon
    objects = models.blogs.objects.all()
    for obj in objects:
        if obj.id == req_id:
            if icon == "love":
                obj.love = obj.love + 1
            elif icon == "like":
                obj.like = obj.like + 1
            else:
                obj.dislike = obj.dislike + 1
            obj.save()
    return redirect('index')


def download(request,type):
    if type == 'user':
        user = request.session['username']
        objects = (models.blogs.objects
                   .filter(uname=user)
                   .values('title', 'category', 'uname', 'date', 'text', 'love', 'like', 'dislike'))
    else:
        objects = (models.blogs.objects
                   .values('title','category','uname','date','text','love','like','dislike'))
    file_content = ''.join("\n\n\t\t\t\tHere are the published Blogs !\n\n\n\n")
    for i in objects:
        file_content = file_content + ("Title : {}\n".format(i['title']))
        file_content = file_content + ("Category : {}\n".format(i['category']))
        file_content = file_content + ("Author : {}\n".format(i['uname']))
        file_content = file_content + ("Created on : {}\n".format(i['date']))
        file_content = file_content + ("Content : {}\n".format(i['text']))
        file_content = file_content + ("Loved By : {}\n".format(i['love']))
        file_content = file_content + ("Liked By : {}\n".format(i['like']))
        file_content = file_content + ("Disliked By : {}\n".format(i['dislike']))
        file_content = file_content + ("\n**************************\n")
        file_content = file_content + ("\n\n\n")
    response = HttpResponse(file_content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename= Blogs.txt'
    return response



@login_required(login_url=reverse_lazy("login_page"))
def index(request):
    main = models.blogs.objects.all()
    response = {
        "published" : main,
        "username" : request.session['username']
    }
    return render(request,'blogs/index.html',context=response)

@login_required(login_url=reverse_lazy("login_page"))
def drafts(request):
    drafts = models.drafts.objects.filter(uname=request.session['username']).values()
    response = {
        "drafts" : drafts
    }
    return render(request,'blogs/drafts.html',context=response)


@login_required(login_url=reverse_lazy("login_page"))
def myblogs(request):
    blogs = models.blogs.objects.filter(uname=request.session['username']).values()
    response = {
        "blogs" : blogs
    }
    return render(request,'blogs/myblogs.html',context=response)


@login_required(login_url=reverse_lazy("login_page"))
def user_logout(request):
    logout(request)
    return HttpResponse(reverse('index'))


def login_page(request):
    message = {"msg": "Incorrect password, please try again!"}
    if request.method == 'POST':
        # message = {"msg": "Incorrect password, please try again!"}
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        print("user var:{} ".format(user))
        if user is not None:
            print('User is active')
            login(request,user)
            request.session['username'] = username
            request.session['password'] = password
            print('session starts')
            print(request.session['username'],request.session['password'])
            request.session['access_level'] = 'admin' if user.is_superuser else 'user'
            return HttpResponseRedirect(reverse('index'))
            # else:
            #     message = {"msg":"No Such Account Active!"}
            #     render(request,'blogs/login.html',context=message)
        else:
            message = {"msg": "Incorrect password, please try again Or No such Account!"}
            print('Username : {} and Password : {}'.format(username,password))
            return render(request,'blogs/login.html',context=message)
    else:
        message = {"msg": "Please login and start Bloggin'"}
        return render(request,'blogs/login.html',context=message)

@login_required(login_url=reverse_lazy("login_page"))
def logout_page(request):
    # if not request.session.is_empty():
    #    return redirect('home')
    username = request.session['username']
    password = request.session['password']
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            print('Session terminated for {} - {}'.format(request.session['username'],request.session['password']))
            del request.session['username']
            request.session.modified = True
            logout(request)
            return HttpResponseRedirect(reverse('login_page'))
        else:
            return HttpResponse('Account Not Active to Logout')
    else:

        error = {}
        error = {"msg": "No such user! "}
        print('Username : {} and Password : {}'.format(username,password))
        return render(request,'blogs/index.html')


@login_required(login_url=reverse_lazy("login_page"))
def newblog(request):
    if request.method == 'POST':
        # print(request.POST)
        type = request.POST.get('drone')
        if type == 'publish':
            form = models.blogs()
            form.title = request.POST.get('title')
            form.category = request.POST.get('category')
            form.text = request.POST.get('text')
            form.uname = request.session['username']
            form.save()
        else:
            form = models.drafts()
            form.title = request.POST.get('title')
            form.category = request.POST.get('category')
            form.text = request.POST.get('text')
            form.uname = request.session['username']
            form.save()
        return redirect('newblog')
    else:
        form = models.blogs()
        frm = {"form":form}
        return render(request, 'blogs/newblog.html',context=frm)


def sign_up(request):
    context = request.POST
    registered = False
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            try:
                user.set_password(user.password)
                user.save()
            except IntegrityError as e:
                user.delete()
                return HttpResponse(e.message)
            registered = True
        else:
            print("User is not Valid!")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'blogs/sign_up.html', {'form': user_form,'registered': registered})

    # if request.method == 'POST':
    #     form = forms.UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()  # Save user to Database
    #         username = form.cleaned_data.get('username')  # Get the username that is submitted
    #         return HttpResponseRedirect(reverse('index'))  # Redirect user to Homepage
    # else:
    #     form = forms.UserRegistrationForm()
    # return render(request, 'blogs/sign_up.html', {'form': form})



