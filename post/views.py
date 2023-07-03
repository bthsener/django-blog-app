from django.shortcuts import render, HttpResponse, get_object_or_404
from post.models import Post

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_details(request):
    get_object_or_404(Post, id=1)
    return HttpResponse("<b>burası post details sayfası</b>")

def post_create(request):
    return HttpResponse("<b>burası post create sayfası</b>")

def post_update(request):
    return HttpResponse("<b>burası post update sayfası</b>")

def post_delete(request):
    return HttpResponse("<b>burası post delete sayfası</b>")

