from django.urls import reverse
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import CommentModels,SubCommentModels, PostModel, ContactFormModel
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    posts = PostModel.objects.all().order_by('-id')
    return render(request, 'blog_app/homepage.html', {"posts" : posts})

def single_post(request, id):
    post = PostModel.objects.get(id=id)
    comments = CommentModels.objects.filter(post=post).order_by("-id")
    context = {
        "post":post,
        "comments": comments
    }
    return render(request, 'blog_app/single_page.html', context)


@login_required
@require_http_methods(["POST"])
def add_comment(request, post_id):
    post_obj = PostModel.objects.get(id=post_id)
    comment_obj = CommentModels(post=post_obj, owner=request.user, comment_body=request.POST["msg"])
    comment_obj.save()
    return HttpResponseRedirect(reverse("blog_app:single_post", args=(post_id,)))



@login_required
@require_http_methods(["POST"])
def add_comment(request, post_id):
    post_obj = PostModel.objects.get(id=post_id)
    comment_obj = SubCommentModels(post=post_obj, owner=request.user, comment_body=request.POST["msg"])
    comment_obj.save()
    return HttpResponseRedirect(reverse("blog_app:single_post", args=(post_id,)))
    

@require_http_methods(["POST","GET"])
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username or not password:
             return render(request, 'blog_app/login.html',{"msg" : "Both Username and Password require to Login."})
        else:     
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("blog_app:homepage"))
            else:
                return render(request, 'blog_app/login.html', {"msg" : "Invalid Username and Password."})

    elif request.method == "GET":
        msg = request.GET.get("msg")
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("blog_app:homepage"))
        return render(request, 'blog_app/login.html',{"msg":msg})

@require_http_methods(["POST","GET"])
def signup(request):
    if request.method =="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if not username or not email or not password or not confirm_password:
            return render(request, 'blog_app/signup.html',{"msg" : "All fields are mandatory for sign up."})
        elif password != confirm_password:
            return render(request, 'blog_app/signup.html',{"msg" : "Password and Confirm Password is  not match."})
        elif User.objects.filter(username=username).exists():
            return render(request, 'blog_app/signup.html',{"msg" : "Username already exists, Please use different username."})
        elif User.objects.filter(email=email).exists():
             return render(request, 'blog_app/signup.html',{"msg" : "Email already exists, Please use different Email."})
        else:
            user = User.objects.create_user(username, email, password)
            return HttpResponseRedirect(reverse("blog_app:login_user") + "?msg=User Created Successfully. Please Login")
    else:
        return render(request, 'blog_app/signup.html', {})
    
    

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("blog_app:login_user"))

def aboutpage(request):
    return render(request, 'blog_app/aboutpage.html', {})
   
def contactpage(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = ContactFormModel(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, 'blog_app/contact.html', {})
    
def blogpage(request):
    posts = PostModel.objects.all().order_by('-id')
    return render(request, 'blog_app/blog.html', {"posts" : posts})

 