from django.contrib import admin
from .models import Meeting, MeetingHost, MeetingMember, Schedule


admin.site.register(Meeting)
admin.site.register(MeetingHost)
admin.site.register(MeetingMember)
admin.site.register(Schedule)
