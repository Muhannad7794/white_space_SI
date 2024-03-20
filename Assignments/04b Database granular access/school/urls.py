from rest_framework.routers import DefaultRouter
from .views import *
from .models import *
from .serializers import *
from django.urls import path

router = DefaultRouter()
router.register(r"campuses", CampusViewSet)
router.register(r"majors", MajorViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"students", StudentViewSet)

urlpatterns = router.urls