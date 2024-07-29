from django.db import transaction

from schedule.models import Meeting, Schedule
from schedule.repository.schedule_repository import ScheduleRepository


class ScheduleComponent:
    @staticmethod
    def create_schedule(schedule_data):
        return ScheduleRepository.create_schedule(schedule_data)

    @staticmethod
    def update_schedule(schedule_data, schedule_id):
        return ScheduleRepository.update_schedule(schedule_data, schedule_id)