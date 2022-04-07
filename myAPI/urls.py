from django.urls import URLPattern, include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('vehicles', views.vehiclesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]