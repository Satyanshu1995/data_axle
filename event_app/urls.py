from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'email-logs', EmailLogViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'template', EmailTemplateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
