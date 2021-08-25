from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render, reverse
from .models import Post
from datetime import *
from .filters import NewsFilter
from .forms import PostForm
from django.views.generic.edit import CreateView
from django.views import View
from django.http import HttpResponse
from .tasks import hello

class NewsList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 3
    form_class = PostForm

    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['filter'] = self.get_filter()
        context['value1'] = None
        context['all_posts'] = Post.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса


        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class SearchNews(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 3

    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        context['time_now'] = datetime.utcnow()
        context['all_posts'] = Post.objects.all()
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_post'
    template_name = 'post_create.html'
    form_class = PostForm


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'news.change_post'
    template_name = 'post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'


class IndexView(View):
    def get(self, request):
        hello.delay()
        return HttpResponse('hello')

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')




