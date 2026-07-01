from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

router = DefaultRouter()
# This registers the viewset and automatically creates the URLs
router.register(r'courses', CourseViewSet)

urlpatterns = router.urls