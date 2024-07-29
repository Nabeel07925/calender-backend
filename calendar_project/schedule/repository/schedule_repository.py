from django.db import transaction

from schedule.models import Meeting, Schedule


class ScheduleRepository:
    @staticmethod
    def create_schedule(schedule_data):
        with transaction.atomic():
            meeting_data = schedule_data.get('meeting')
            meeting = Meeting.objects.create(
                title=meeting_data.get('title'),
                description=meeting_data.get('description')
            )

            schedule = Schedule.objects.create(
                date=schedule_data.get('date'),
                start_time=schedule_data.get('start_time'),
                end_time=schedule_data.get('end_time'),
                meeting=meeting
            )
            schedule.save()
            return schedule

    @staticmethod
    def update_schedule(schedule_data, schedule_id):
        with transaction.atomic():
            schedule = Schedule.objects.get(id=schedule_id)
            meeting = schedule.meeting
            for attr_, value in schedule_data.get('meeting').items():
                setattr(meeting, attr_, value)
            meeting.save()

            schedule_data.pop('meeting')
            for attr_, value in schedule_data.items():
                setattr(schedule, attr_, value)

            schedule.save()
            return schedule
