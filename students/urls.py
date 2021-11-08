from rest_framework.routers import SimpleRouter

from .views import StudentViewSet, StudentDocumentViewSet

router = SimpleRouter()

router.register('students', StudentViewSet)
router.register('documents', StudentDocumentViewSet)

urlpatterns = []

urlpatterns += router.urls
