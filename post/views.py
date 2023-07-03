from django.shortcuts import render, HttpResponse, get_object_or_404
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
    form = PostForm()
    context={
        'form': form,
    }
    # if request.method=="POST":
    #    print(request.POST)

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Post.objects.create(title=title,content=content)
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm
        print("alanlari doldur")

    return render(request,'post/form.html',context)

def post_update(request):
    return HttpResponse("<b>burası post update sayfası</b>")

def post_delete(request):
    return HttpResponse("<b>burası post delete sayfası</b>")