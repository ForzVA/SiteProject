from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    obscences = ['церковь', 'Путин', 'Украина']
    for obs in obscences:
       value = value.replace(obs, (obs[0] + "*"*(len(obs)-2) + obs[-1]))
    return value
