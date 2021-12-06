from rest_framework import serializers

from .models import Student, StudentDocument

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'worker', 'surname', 'name', 'patronymic', 'date_of_birth',
                    'fio_parents', 'phone_number', 'email', 'status', 'date', 'color']

class StudentDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentDocument
        fields = ['id', 'student', 'document_type', 'file']
