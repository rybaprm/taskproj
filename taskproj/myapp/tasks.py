from __future__ import absolute_import, unicode_literals
from time import sleep

from django.core.mail import send_mail
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def sleeped(duration):
    sleep(duration)


@shared_task
def send_email_task():
    sleep(10)
    send_mail(
        'Test',
        'This is test message',
        '20celery20@gmail.com',
        ['uiyfbskyldqrrjillq@awdrt.org']
    )