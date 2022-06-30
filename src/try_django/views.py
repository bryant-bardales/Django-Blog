from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
# Don't Repeat Yourself = DRY

from blog.models import BlogPost


def home_page(request):
    qs = BlogPost.objects.all()[:5]
    context = {"blog_list": qs}  # Blog listing
    return render(request, "home.html", context)


def about_view(request):
    return render(request, "about.html", )
