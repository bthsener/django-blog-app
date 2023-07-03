from django.shortcuts import render, HttpResponse

# Create your views here.
def post_index(request):
    return HttpResponse("<b>burası post index sayfası</b>")

def post_details(request):
    return HttpResponse("<b>burası post details sayfası</b>")

def post_create(request):
    return HttpResponse("<b>burası post create sayfası</b>")

def post_update(request):
    return HttpResponse("<b>burası post update sayfası</b>")

def post_delete(request):
    return HttpResponse("<b>burası post delete sayfası</b>")

