from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from schedule.models import Meeting, MeetingHost, MeetingMember, Schedule


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MeetingMemberSerializer(ModelSerializer):

    class Meta:
        model = MeetingMember
        fields = '__all__'


class MeetingSerializer(ModelSerializer):
    meeting_members = MeetingMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = '__all__'


class MeetingHostSerializer(ModelSerializer):

    class Meta:
        model = MeetingHost
        fields = '__all__'


class ScheduleSerializer(ModelSerializer):
    meeting = MeetingSerializer(read_only=True, many=False)
    meeting_id = serializers.PrimaryKeyRelatedField(
        queryset=Meeting.objects.all(),
        source='meeting', write_only=True
    )

    class Meta:
        model = Schedule
        fields = '__all__'
