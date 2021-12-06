from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_to_worker(user, student):
    send_mail(subject='New Student',
              from_email=None,
              message=f'You have received a studentto work on. {student.surname}',
              recipient_list=[user.email, ])
