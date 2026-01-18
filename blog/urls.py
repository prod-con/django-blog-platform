from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', views.create_article, name='create_article'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('user/<str:username>/', views.user_articles, name='user_articles'),
]
