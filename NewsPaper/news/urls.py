from django.urls import path
from .views import (NewsList, NewsDetail, SearchNews, PostCreate, PostDelete, PostUpdate )

urlpatterns = [path('', NewsList.as_view()),
               path('search/', SearchNews.as_view()),
               path('<int:pk>/', NewsDetail.as_view(), name='post_detail'),
               path('add/', PostCreate.as_view(), name='post_create'),
               path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
               path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
               ]