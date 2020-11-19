from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from posts.models import *
from posts.forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(Q(title__icontains=query) | Q(content__icontains=query))
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)
    context = {
        'posts': post_list
    }
    return render(request, "post/index.html", context)


def detail(request, id):
    context = {
        'post': get_object_or_404(Post, id=id)
    }
    return render(request, "post/detail.html", context)


@login_required(login_url='/')
def create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'post/create.html', context)


@login_required(login_url='/')
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('/')


@login_required(login_url='/')
def update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'post/update.html', context)
