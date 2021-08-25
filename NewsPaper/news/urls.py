from django.urls import path
from .views import (NewsList, NewsDetail, SearchNews, PostCreate, PostDelete, PostUpdate, upgrade_me, IndexView)
from django.contrib.auth.views import LogoutView

urlpatterns = [path('', NewsList.as_view()),
               path('search/', SearchNews.as_view()),
               path('<int:pk>/', NewsDetail.as_view(), name='post_detail'),
               path('add/', PostCreate.as_view(), name='post_create'),
               path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
               path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
               path('upgrade/', upgrade_me, name='upgrade'),
               path('accounts/logout/', LogoutView.as_view(template_name='flatpages/home.html'), name='logout'),
               path('cow/', IndexView.as_view()),
            ]
