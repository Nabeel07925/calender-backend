from schedule.repository.meeting_repository import MeetingRepository


class MeetingComponent:
    @staticmethod
    def get_meetings():
        return MeetingRepository.get_meetings()
