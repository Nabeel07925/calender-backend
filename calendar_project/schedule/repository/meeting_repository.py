from schedule.models import Meeting


class MeetingRepository:
    @staticmethod
    def get_meetings():
        return Meeting.objects.select_related('meeting_members').all()
