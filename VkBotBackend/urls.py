from django.contrib import admin
from django.urls import path, include
from day_app.views import StudentViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/day_app/', include(router.urls))
]
