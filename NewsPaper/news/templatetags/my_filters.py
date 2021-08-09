from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    obscences = ['-------',]
    for obs in obscences:
       value = value.replace(obs, '*****')
    return value
