from rest_framework import routers
from django.urls import path, include
from schedule.views import UserViewSet, MeetingViewSet, ScheduleViewSet, MeetingHostViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'/users', UserViewSet, basename="users")
router.register(r'/meeting', MeetingViewSet)
# router.register('meeting_member', MeetingMemberViewSet)
router.register('/meeting_host', MeetingHostViewSet)
router.register(r'/schedule', ScheduleViewSet)


urlpatterns = [
    path('/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]