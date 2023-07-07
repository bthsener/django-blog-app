from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from post.models import Post
from .form import PostForm, CommentForm
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_index(request):
    postlist = Post.objects.all()
    paginator = Paginator(postlist, 25)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator)

    return render(request, 'post/index.html', {'posts': posts})

def post_details(request, id):
    get_object_or_404(Post, id=id)
    postRef = Post.objects.get(id=id)

    form = CommentForm(request.POST or None)
    #
    # if form.is_valid():
    #     comment = form.save(commit=False)
    #     comment.post = postRef
    #     comment.save()
    #     return HttpResponseRedirect(postRef.get_absolute_url)

    context = {
        'post': postRef,
        # 'form': form,
    }

    return render(request, 'post/details.html', context)

def post_create(request):
    # if not request.user.is_authenticated():
    #     return Http404

    # form = PostForm()

    # if request.method=="POST":
    #    print(request.POST)
    #
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Post.objects.create(title=title,content=content)
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        # form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm
        print("alanlari doldur")

    context = {
        'form': form,
    }
    return render(request,'post/form.html', context)

def post_update(request, id):
    # if not request.user.is_authenticated():
    #     return Http404

    postRef = Post.objects.get(id= id)
    form = PostForm(request.POST or None,  request.FILES or None, instance=postRef)

    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)

def post_delete(request, id):
    # if not request.user.is_authenticated():
    #     return Http404

    postRef = get_object_or_404(Post, id=id)
    postRef.delete()

    return HttpResponseRedirect('/post/index/')

def comment_create(request, id):
    get_object_or_404(Post, id=id)
    post_ref = Post.objects.get(id=id)

    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post_ref
        comment.save()

    context = {
        'post': post_ref,
        'form': form,
    }

    return render(request, 'post/details.html', context)
