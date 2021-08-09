from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from . import filters
from .models import Post
from datetime import *
from .filters import NewsFilter
from .forms import PostForm



class NewsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 3
    form_class = PostForm

    def get_filter(self):
        return NewsFilter(self.request.GET, queryset = super().get_queryset())

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

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class NewsDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class SearchNews(ListView):
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


class PostCreate(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm


class PostUpdate(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'


