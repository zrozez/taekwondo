from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Student, StudentDocument
from .serializers import StudentSerializer, StudentDocumentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny, ]

class StudentDocumentViewSet(ModelViewSet):
    queryset = StudentDocument.objects.all()
    serializer_class = StudentDocumentSerializer
    permission_classes = [AllowAny, ]