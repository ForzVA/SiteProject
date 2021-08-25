from django.db.models.signals import *
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import Post
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.contrib.auth.models import User

@receiver(post_save, sender=Post)
def sub_mail(sender, instance, created, **kwargs):
    html_content = render_to_string('post_created.html',
                                    {'post': Post}
                                     )
    msg = EmailMultiAlternatives(subject=f'{User.email}',
                                 body=f'{User.username}',
                                 from_email='Forz00@yandex.by',
                                 to=['vasilevskiysasha1@gmail.com']
                                 )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()