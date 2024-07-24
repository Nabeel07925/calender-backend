from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from schedule import serializers
from schedule.models import Meeting, MeetingMember, Schedule, MeetingHost
from schedule.serializers import UserSerializer, MeetingSerializer, MeetingMemberSerializer, MeetingHostSerializer, \
    ScheduleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [permissions.AllowAny]


# class MeetingMemberViewSet(serializers.ModelSerializer):
#     queryset = MeetingMember.objects.all()
#     serializer_class = MeetingMemberSerializer


class MeetingHostViewSet(viewsets.ModelViewSet):
    queryset = MeetingHost.objects.all()
    serializer_class = MeetingHostSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.AllowAny]
