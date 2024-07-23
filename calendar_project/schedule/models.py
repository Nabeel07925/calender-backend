import pytz
from django.db import models
from django.contrib.auth.models import User
from calendar_project.models import BaseModel


class Meeting(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, null=True)


class MeetingHost(BaseModel):
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE,
                                   related_name='meeting_host')
    host = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='meeting_host')


class MeetingMember(BaseModel):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE,
                                related_name='meeting_members')
    member = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='meeting_members')


class Schedule(BaseModel):
    date = models.DateField()
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE,
                                   related_name='schedules')
    start_time = models.TimeField()
    end_time = models.TimeField()
    timezone = models.CharField(max_length=50, choices=[(tz, tz) for tz in pytz.all_timezones], default='UTC')
