from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    obscences = ['получат', 'недель', 'полет']
    for obs in obscences:
       value = value.replace(obs, '*****')
    return value
