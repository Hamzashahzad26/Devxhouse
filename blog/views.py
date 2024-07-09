from django.shortcuts import render

# Create your views here.
from django.views import generic  
from blog.models import *




# def blog(request):
#     return render(request, "blog.html")



# def article(request):
#     return render(request, "article.html")


class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-create_on')
  template_name = 'blog.html'


class DetailView(generic.DetailView):
  model = Post
  template_name = 'article.html'
  

