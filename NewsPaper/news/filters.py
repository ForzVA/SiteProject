import django_filters
from .models import Post
from django.forms import DateInput


class NewsFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='dateCreation', widget=DateInput(attrs={'type': 'date'}),
                                     lookup_expr='gt', label='Date of creation(without today)')

    class Meta:
        model = Post
        fields = {'author': ['exact'],
                  'title': ['icontains'],}







