from constance.admin import config
from django.shortcuts import render
from django.views import View, generic
from django.views.generic import DetailView, ListView

from .models import *
from django.db.models import Q
from django.core.mail import send_mail


class IndexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        # stories = Blog.objects.all()
        recent_post = Blog.objects.all().order_by('-pub_date')[:4]
        blog = Blog.objects.order_by('-pub_date')[4:]
        """Handle GET requests: instantiate a blank version of the form."""
        return render(request, 'index.html', {'blog': blog, 'recent_post': recent_post})


class IndexDetailView(DetailView):
    template_name = "post.html"
    model = Blog


class PostView(generic.ListView):
    template_name = 'post.html'
    model = Blog
    context_object_name = 'blog'


class AuthorView(generic.ListView):
    template_name = 'author.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["config"] = config
        return context


class AuthorDetailView(generic.ListView):
    template_name = 'authordetail.html'
    model = Blog

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.filter(user_id=kwargs.get('user_id'))
        user = User.objects.filter(id=kwargs.get('user_id'))
        return render(request, self.template_name, {'blog': blog, 'user': user})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["config"] = config
        return context


class SearchView(generic.ListView):
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET['query']
        allpost = Blog.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return allpost
