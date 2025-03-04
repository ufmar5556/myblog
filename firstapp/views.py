from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    return render(request, "firstapp/home.html")

def index(request):
    return render(request, "firstapp/index.html")

def about(request):
    return render(request, "firstapp/about.html")

def post_list(request):
    posts = Post.objects.all().order_by('-date_published')  # Get all posts, newest first
    return render(request, 'firstapp/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "firstapp/post_detail.html", {"post": post})

def create_post(request):
    if request.method == "POST":
        print("Received POST request:", request.POST)  # Debugging
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save to the database yet
            post.save()  # Automatically assigns date_published
            print("Form saved successfully!")  # Debugging
            return redirect('post_list')
        else:
            print("Form errors:", form.errors)  # Debugging
    else:
        form = PostForm()

    return render(request, 'firstapp/create_post.html', {'form': form})