from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime
from .models import Category, Topic, Tag, Post, Page


def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj Sasza! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)


def category_list(request):
    categories = Category.objects.all()

    return render(request,
                  "posts/category/list.html",
                  {'categories': categories})


def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404("Obiekt Category o podanym id nie istnieje")

    return render(request,
                  "posts/category/detail.html",
                  {'category': category})


def topic_list(request):
    topics = Topic.objects.all()
    return render(request,
                  "posts/topic/list.html",
                  {'topics': topics})


def topic_detail(request, id):
    try:
        topic = Topic.objects.get(id=id)
    except Topic.DoesNotExist:
        raise Http404("Obiekt Topic o podanym id nie istnieje")

    return render(request,
                  "posts/topic/detail.html",
                  {'topic': topic})


def tag_list(request):
    tags = Tag.objects.all()

    return render(request,
                  "posts/tag/list.html",
                  {'tags': tags})


def tag_detail(request, id):
    try:
        tag = Tag.objects.get(id=id)
    except Tag.DoesNotExist:
        raise Http404("Obiekt Tag o podanym id nie istnieje")

    return render(request,
                  "posts/tag/detail.html",
                  {'tag': tag})


def post_list(request):
    posts = Post.objects.all()

    return render(request,
                  "posts/post/list.html",
                  {'posts': posts})


def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Obiekt Post o podanym id nie istnieje")

    return render(request,
                  "posts/post/detail.html",
                  {'post': post})


def page_list(request):
    pages = Page.objects.all()

    return render(request,
                  "posts/page/list.html",
                  {'pages': pages})


def page_detail(request, id):
    try:
        page = Page.objects.get(id=id)
    except Page.DoesNotExist:
        raise Http404("Obiekt Page o podanym id nie istnieje")

    return render(request,
                  "posts/page/detail.html",
                  {'page': page})