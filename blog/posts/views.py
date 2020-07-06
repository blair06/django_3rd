from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {"post":posts[0]})
