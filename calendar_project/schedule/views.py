from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from schedule import serializers
from schedule.components.meeting_component import MeetingComponent
from schedule.components.schedule_component import ScheduleComponent
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

    def list(self, request, *args, **kwargs):
        meetings = MeetingComponent.get_meetings()
        meetings_serializer = MeetingSerializer(meetings, many=True)
        return Response(meetings_serializer.data, status=status.HTTP_200_OK)


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

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            schedule = ScheduleComponent.create_schedule(schedule_data=data)
            schedule_serializer = ScheduleSerializer(schedule, many=False)
            return Response({
                "data": schedule_serializer.data,
                "message": "Schedule created successfully"
            },
                content_type='application/json',
                status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), content_type='application/json',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            data = request.data
            schedule_id = kwargs.get('pk')
            schedule = ScheduleComponent.update_schedule(schedule_data=data, schedule_id=schedule_id)
            schedule_serializer = ScheduleSerializer(schedule, many=False)
            return Response({
                "data": schedule_serializer.data,
                "message": "Schedule updated successfully"
            },
                content_type='application/json',
                status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), content_type='application/json',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
