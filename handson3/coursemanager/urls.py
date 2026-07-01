from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This includes the URLs from your courses app
    path('api/', include('courses.urls')),
]