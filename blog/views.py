from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Blog, Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm, CreateUserForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def blog_list(request):
    posts = Blog.objects.all()
    carousel = Blog.objects.all().order_by('-id')[:4]
    return render(request, 'list.html',{'posts':posts, 'carousel':carousel})

@login_required(login_url='login')
def blog_detail(request, pk):
    posts = get_object_or_404(Blog, pk=pk)
    comments = posts.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.posts = posts
            comment.save()

            return redirect('detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'posts':posts, 'form':form, 'comments':comments})

@login_required(login_url='login')
def post_like(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.likes +=1
    post.save()
    return redirect('detail', pk=pk)

@login_required(login_url='login')
def search(request):
    query = request.GET.get('q', '')
    results = Blog.objects.filter(title__icontains=query) #case insensitive

    return render(request, 'search.html', {'query':query, 'results':results})