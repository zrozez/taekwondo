from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

import environ
import smtplib, ssl

from .models import Student, StudentDocument
from .serializers import StudentSerializer, StudentDocumentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny, ]
    filter_backends=(DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ['id', ]
    search_fields = ['surname', 'name', ]

    def reminder(self, receiver_email, message):
        student = self.get_object()
        env = environ.Env()
        port = env('EMAIL_HOST_PORT')
        smtp_server = "smtp.gmail.com"
        sender_email = env('EMAIL_HOST_USER')
        receiver_email = receiver_email
        password = env('EMAIL_HOST_PASSWORD')
        message = message
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return Response({'success': True})


    @action(methods=['get', ], detail=True)
    def parent_reminder(self, request, *args, **kwargs):
        student = self.get_object()
        self.reminder(student.email, f"Uchenik {student.surname} {student.name} uspeshno prinyat v gruppu!")
        return Response({'success': True})

    @action(methods=['get', ], detail=True)
    def teacher_reminder(self, request, *args, **kwargs):
        student = self.get_object()
        self.reminder(student.worker.email, f"{student.surname} {student.name} podal zayavku!")
        return Response({'success': True})

class StudentDocumentViewSet(ModelViewSet):
    queryset = StudentDocument.objects.all()
    serializer_class = StudentDocumentSerializer
    permission_classes = [AllowAny, ]