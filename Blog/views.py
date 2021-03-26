from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Blog
from .forms import BlogForm

# Create your views here.

def showBlog(request):
    blogs=Blog.objects.all()
    context={
        'blogs':blogs
    }
    return render(request, 'Blog/Blogs.html', context)

@login_required
def insertBlog(request):
    form = BlogForm()
    message = ""
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        message = "invalid input. Please try again"
        if form.is_valid():
            blogs = form.save(commit=False)

            blogs.user = request.user
            blogs.save()

            message="Blog is added"
            form=BlogForm()

    context = {
        'form':form,
        'message':message
    }

    return render(request, 'Blog/InsertBlog.html', context)

