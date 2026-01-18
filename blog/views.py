from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Article

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})

def user_articles(request, username):
    user = get_object_or_404(User, username=username)
    articles = Article.objects.filter(author=user)
    return render(request, 'blog/user_articles.html', {'articles': articles, 'author': user})

def article_detail(request, article_id):
    # FLAW 1: Always shows the first article instead of the requested one!
    article = Article.objects.first()

    # FLAW 2: No authorization check - any logged-in user can delete any article!
    if request.method == 'POST' and request.POST.get('action') == 'delete':
        if request.user.is_authenticated:
            article.delete()
            return redirect('home')

    return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Article.objects.create(title=title, content=content, author=request.user)
            return redirect('home')
    return render(request, 'blog/create_article.html')

@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user)
    if request.method == 'POST':
        article.delete()
        return redirect('home')
    return render(request, 'blog/delete_article.html', {'article': article})
