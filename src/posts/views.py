import json
from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from .forms import  PostForm
from profiles.models import Profile

# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def post_list_and_create(request):
    # qs = Post.objects.all()
    form = PostForm(request.POST or None)
    if is_ajax(request=request):
        
        if form.is_valid():
            author = Profile.objects.get(user =request.user)
            instance = form.save(commit=False)
            instance.author = author
            instance.save()
            return JsonResponse({
                'title' : instance.title,
                'body' : instance.body,
                'author' : instance.author.user.username,
                'id' : instance.id,
            })

    context = {
        'form'  : form
    }
    return render(request,'posts/main.html',context)


def post_detail(request,pk):
    obj = Post.objects.get(pk = pk)
    form = PostForm()
    context = {
        'obj' : obj,
        'form' : form,
    }

    return render(request,'posts/detail.html',context)

def post_detail_data_view(request,pk):
    obj = Post.objects.get(pk=pk)
    data = {
        'id' : obj.id,
        'title' : obj.title,
        'body' : obj.body,
        'author' : obj.author.user.username,
        'logged_in' : request.user.username,

    }
    return JsonResponse({'data' : data})

def load_post_data_view(request,num_posts):
    if is_ajax(request = request):
        visible = 3
        upper = num_posts
        lower = upper - visible
        size = Post.objects.all().count()
        qs = Post.objects.all()
        data = []
        for obj in qs:
            item = {
                'id'  : obj.id,
                'title'  : obj.title,
                'body' : obj.body,
                'author' : obj.author.user.username,
                'liked' : True if request.user in obj.liked.all()  else False,
                'count' : obj.like_count,
            }
            data.append(item)
        
        return JsonResponse({'data':data[lower:upper],'size' : size})


def like_unlike_post(request):
    if is_ajax(request=request):
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        return JsonResponse({'liked':liked,'count' : obj.like_count})


def update_post(request,pk):
    obj = Post.objects.get(pk=pk)
    if is_ajax(request):
        new_title = request.POST.get('title')
        new_body = request.POST.get('body')
        obj.title = new_title
        obj.body = new_body
        obj.save()

    return JsonResponse({'title' : new_title,
        'body': new_body,})
    
def delete_post(request,pk):
    obj = Post.objects.get(pk = pk)
    if is_ajax(request):
        obj.delete()
    return JsonResponse({})
        

    
