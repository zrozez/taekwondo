from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_mail_to_parent(student_email, student_name):
    print(student_email)
    send_mail(subject='Ребенок принят',
            message= f'Студент с именем {student_name} принят в группу',
            recipient_list=[student_email, ],
            from_email=None)