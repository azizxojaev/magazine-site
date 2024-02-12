from django.shortcuts import render, redirect
import datetime
from .utils import get_default_context
import math
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import os


def home_page(request):
    context = {}
    context = get_default_context(context)
    return render(request, 'index.html', context=context)

def category_page(request, tag=None):
    news_obj = New.objects.all()

    active_tag = ''
    active_search = ''
    if tag:
        tag_obj = Tag.objects.get(slug=tag)
        news_obj = news_obj.filter(tag=tag_obj)
        active_tag = tag_obj.slug
    active_search = request.GET.get('q', '')
    if active_search != "":
        news_obj = news_obj.filter(title__icontains=active_search)

    news = [news_obj[i:i+13] for i in range(0, len(news_obj), 13)]
    context = {
        'news': news,
        'active_tag': active_tag,
        'active_search': active_search,
    }
    context = get_default_context(context)
    return render(request, 'category.html', context=context)

def contact_page(request):
    context = {}
    context = get_default_context(context)
    return render(request, 'contact.html', context=context)

def singe_page(request, slug):
    article = New.objects.get(slug=slug)

    if NewsView.objects.get_or_create(user=request.user, article=article)[1] == True:
        article.views = NewsView.objects.filter(article=article).count()
        article.save()
        article = New.objects.get(slug=slug)

    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        message = request.POST.get('message')
        reply_to = request.POST.get('reply_to')
        if reply_to == "":
            Comment.objects.create(user=profile, text=message, article=article)
        else:
            comment_id = int(reply_to.split('_')[1])
            comment = Comment.objects.get(id=comment_id)
            ReplyComment.objects.create(user=profile, text=message, reply_to=comment)

    comments_obj = Comment.objects.filter(article=article)
    comments = []
    for i in comments_obj:
        reply_comments = ReplyComment.objects.filter(reply_to=i)
        if reply_comments:
            comments.append([i, reply_comments])
        else:
            comments.append(i)

    context = {
        'article': article,
        'comments': comments
    }
    context = get_default_context(context)

    return render(request, 'single.html', context=context)

def login_page(request):
    if not request.user.is_authenticated:
        context = {}
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            context = {
                "username": username,
                "password": password
            }
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                context['error'] = "Incorrect username or password"
        return render(request, "login.html", context=context)
    else:
        return redirect("home")

def register_page(request):
    if not request.user.is_authenticated:
        context = {}
        if request.method == "POST":
            username = request.POST.get('username')
            password1 = request.POST.get('password')
            password2 = request.POST.get('repeat_password')
            email = request.POST.get('email')
            context = {
                'username': username,
                'password': password1,
                'repeat_password': password2,
                'email': email
            }
            if len(password1) >= 8:
                if not User.objects.filter(email=email).exists():
                    if not username.isdigit():
                        if not User.objects.filter(username=username).exists():
                            if password1 == password2:
                                user = User.objects.create_user(
                                    username=username, password=password1, email=email
                                )
                                Profile.objects.create(user=user)
                                login(request, user)
                                return redirect("home")
                            else:
                                context['error'] = "Passwords don't match"
                        else:
                            context['error'] = "Username already taken"
                    else:
                        context['error'] = "Username mustn't contain only numbers"
                else:
                    context['error'] = "Email already taken"
            else:
                context['error'] = "Password must be at least 8 characters"
        return render(request, "register.html", context=context)
    else:
        return redirect('home')

def logout_page(request):
    logout(request)
    return redirect('login')

def account_page(request):
    profile = Profile.objects.get(user=request.user)
    news = New.objects.filter(author=profile)

    if request.method == "POST":
        if request.FILES:
            if profile.image != "avatars/default.png":
                old_avatar_path = profile.image.path
                if os.path.exists(old_avatar_path):
                    os.remove(old_avatar_path)
            img = request.FILES.get('image')
            profile.image = img
            profile.save()
            profile = Profile.objects.get(user=request.user)

    context = {
        'profile': profile,
        'news': news
    }
    return render(request, "account.html", context=context)