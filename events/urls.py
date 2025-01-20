from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegisterView, EventDetailsApiView

router = DefaultRouter()
router.register(r'events-details', EventDetailsApiView, basename='events-details')

urlpatterns = [
    path('', include(router.urls)),
    path('user-register/', RegisterView.as_view(), name='user-register'),
]