from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime

NEWS = 'NS'
ARTICLE = 'AR'
CAT_CHOIСES = [
    (NEWS, 'News'),
    (ARTICLE, 'Article')
    ]


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rateAuthor = models.IntegerField(default=0)

    def update_rating(self):
        postRating = self.post_set.aggregate(postRating=Sum('rating'))
        pRating = 0
        pRating += postRating.get('postRating')

        commentRating = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRating = 0
        cRating += commentRating.get('commentRating')

        self.rateAuthor = pRating * 3 + cRating
        self.save()

    def __str__(self):
        return f'{self.authorUser}'


class Category(models.Model):
    nameCategory = models.CharField(unique=True,
                                    max_length=64)

    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.nameCategory}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    categorySelection = models.CharField(choices=CAT_CHOIСES,
                                         default='NS',
                                         max_length=2,
                                         verbose_name='Category')
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(unique=True,
                             max_length=128)
    text = models.TextField(verbose_name='News text')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:128] + '...'

    def __str__(self):
        return f'{self.title}:{self.text[:20]}'

    def get_absolute_url(self):
        return f'/posts/{self.id}'


class PostCategory(models.Model):
    postWay = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryWay = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    textComment = models.TextField(default='Nothing')
    timeComment = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.commentPost}'









