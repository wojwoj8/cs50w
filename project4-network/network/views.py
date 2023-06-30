from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import PostForm
from .models import User, Post, Follow
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    posts = Post.objects.all().order_by('-post_date')
    
    post_pagination = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = post_pagination.get_page(page_number)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = request.POST["post"]
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user = request.user
            #print(user)
            #print(post)
            new_post = Post(post = post, post_date = date, user=user)
            new_post.save()
            form = PostForm()
            return HttpResponseRedirect(reverse("index"))
        else:
            #form = PostForm()
            message = "Post was not added succesfully"
            
    #elif request.method == "PUT":

        return render(request, "network/index.html", {
            'form':form,
            'message':message,
            'page_obj':page_obj,
            })
    else:
        
        form = PostForm()
        return render(request, "network/index.html", {
                'form':form,
                'page_obj':page_obj,
                })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def profile_view(request, uname):
    #access from foreign key to user without id
    posts=Post.objects.filter(user__in = User.objects.filter(username=uname)).order_by('-post_date')
    post_pagination = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = post_pagination.get_page(page_number)
    profile=User.objects.get(username=uname)
    try:
        #logged user
        luser =  request.user.username
        loguser = User.objects.get(username=luser)
        pro=User.objects.get(username=luser)
    except ObjectDoesNotExist:
        pro = None
 
    
    
    if Follow.objects.filter(username=profile, follower=pro).exists():
        button = "Unfollow"
    else:
        button = "Follow"

    if request.method == "GET":
       
        return render(request, "network/profile.html", {
                    
                    "button":button,
                    "name":uname,
                    "profile":profile,
                    'page_obj':page_obj,
                })
    else:
        if not Follow.objects.filter(username=profile, follower=pro).exists():
            new_follow = Follow(username=profile, follower=pro)
            new_follow.save()
            x = profile.followers_nr
            x += 1
            User.objects.filter(username=uname).update(followers_nr = x)

           
            y = loguser.follows_nr
            y += 1
            User.objects.filter(username=luser).update(follows_nr=y)
        else:
            #delete follow
            Follow.objects.filter(username=profile, follower=pro).delete()
            x = profile.followers_nr
            x -= 1
            User.objects.filter(username=uname).update(followers_nr = x)

            y = loguser.follows_nr
            y -= 1
            User.objects.filter(username=luser).update(follows_nr=y)

        return HttpResponseRedirect(reverse("profile", args=(uname,)))

@login_required
def follows(request):
    if request.method == "GET":
        luser = request.user.username
        profile = User.objects.get(username=luser)

        #list of users id followed by logged user 
        foll = Follow.objects.filter(follower=profile).values_list('username_id')


        #posts where user id is in foll
        posts=Post.objects.filter(user__in = User.objects.filter(id__in=foll)).order_by('-post_date')
        post_pagination = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = post_pagination.get_page(page_number)
        #print(posts)
    
        return render(request, "network/follows.html", {
                "profile":profile,
                'page_obj':page_obj,
                "foll":foll,
            })

@login_required
@csrf_exempt
def like(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        #print(post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == "GET":

        if request.user in post.likes.all():

            post.likes.remove(request.user)
        else:

            post.likes.add(request.user)
        post.save()
        #print(post.likes.all())
        return JsonResponse(post.serialize())
    
    return HttpResponse(status=204)




@login_required
@csrf_exempt
def editPost(request, post_id):
     # Query for requested post
    try:
        post = Post.objects.get(user=request.user, pk=post_id)
        #print(post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
    # Return post contents
    if request.method == "GET":
        return JsonResponse(post.serialize())

    elif request.method == "PUT":
        data = json.loads(request.body)
        if data.get("post"):
            post.post = data["post"]
            post.save()
        return HttpResponse(status=204)
