from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from post.models import Post
from .form import PostForm

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_details(request, id):
    get_object_or_404(Post, id=id)
    postRef = Post.objects.get(id=id)
    return render(request, 'post/details.html', {'post': postRef})

def post_create(request):
    # form = PostForm()

    # if request.method=="POST":
    #    print(request.POST)
    #
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Post.objects.create(title=title,content=content)
    form = PostForm(request.POST or None)
    if request.method=="POST":
        # form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm
        print("alanlari doldur")

    context = {
        'form': form,
    }
    return render(request,'post/form.html', context)

def post_update(request, id):
    postRef = Post.objects.get(id= id)
    form = PostForm(request.POST or None, instance=postRef)

    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context= {
        'form': form,
    }

    return render(request, 'post/form.html', context)

def post_delete(request, id):
    postRef = get_object_or_404(Post, id=id)
    postRef.delete()

    return HttpResponseRedirect('/post/index/')