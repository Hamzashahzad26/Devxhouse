# manually creeated file

from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    # path('blog', views.blog, name='blog' ),
    # path('article', views.article, name='article' ),
  path('blog/', views.PostList.as_view(), name="blog"),
  path('<slug:slug>/', views.DetailView.as_view(), name="article"),

    
]