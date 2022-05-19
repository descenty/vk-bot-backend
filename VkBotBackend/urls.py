from django.contrib import admin
from django.urls import path, include
from day_app.views import StudentViewSet, ScheduleWeekViewSet, StudyGroupViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'students', StudentViewSet)
#router.register(r'study_groups', StudyGroupViewSet)
router.register(r'schedule_weeks', ScheduleWeekViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/day_app/', include(router.urls)),
]
