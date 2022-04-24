from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ProjectViewSet, CustomerViewSet,
                    BankViewSet, CheckViewSet)


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'banks', BankViewSet, basename='banks')
router.register(r'checks', CheckViewSet, basename='checks')

urlpatterns = [
    path('', include(router.urls))
]
