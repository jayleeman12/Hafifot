"""Logger module"""
from typing import Dict
from abc import ABC
from datetime import datetime
from datetimerange import DateTimeRange
from Hafifot.Solution.Error import AlreadyExistsError, NotFoundError


class Event:
    def __init__(self, event_id: int, date: datetime.date, time_range: DateTimeRange, location: str):
        self.date = date
        self.time_range = time_range
        self.location = location
        self.event_id = event_id

    def get_date(self) -> datetime.date:
        return self.date

    def set_date(self, date: datetime.date):
        self.date = date

    def get_time_range(self) -> DateTimeRange:
        return self.time_range

    def set_time_range(self, time_range: DateTimeRange):
        self.time_range = time_range

    def get_location(self) -> str:
        return self.location

    def set_location(self, location: str):
        self.location = location

    def get_id(self) -> int:
        return self.event_id

    def set_id(self, event_id: int):
        self.event_id = event_id


class Logger(ABC):
    """Base class for this module"""

    def __init__(self, events: Dict):
        self.events = events

    def get_events(self) -> Dict:
        return self.events

    def set_events(self, events: Dict):
        self.events = events

    def add_event(self, event: Event):
        if event.get_id() in self.events:
            raise AlreadyExistsError("already exists in the Corona logger")
        self.events[event.get_id()] = event

    def delete_event(self, event_id: int):
        if event_id not in self.events:
            raise NotFoundError("event not fount in the Corona logger")
        del self.events[event_id]


class CoronaLogger(Logger):
    """Corona Logger to keep track of corona infected locations"""

    def __init__(self, events: Dict, incubation_period: int):
        super().__init__(events)
        self.incubation_period = incubation_period

    def get_incubation_period(self) -> int:
        return self.incubation_period

    def set_incubation_period(self, incubation_period: int):
        self.incubation_period = incubation_period


class CoronaCollisionChecker:

    @staticmethod
    def is_infected(logger: CoronaLogger, event: Event) -> bool:
        """Given an event check in the logger if there are intersections"""

        for event_id, record in logger.get_events():
            if record.get_time_range().is_intersection(event.get_time_range()):
                return True

        return False

    @staticmethod
    def add_infected_record(logger: CoronaLogger, location_history: Dict):
        """Add a person event list to the logger"""

        for event_id, record in location_history:
            try:
                logger.add_event(record)

            except AlreadyExistsError as e:
                print(f'Event with event id: {event_id} {e.message}')

    @staticmethod
    def enter_isolation(logger: CoronaLogger, location_history: Dict) -> int:
        """Given a location history check if the person need to enter isolation, """
        delta = 0
        for event_id, record in location_history:
            if CoronaCollisionChecker.is_infected(logger, record):
                days_post_incident = (datetime.today() - record.get_date()).days
                if days_post_incident < logger.get_incubation_period():
                    if delta < days_post_incident:
                        delta = days_post_incident

        return logger.get_incubation_period() - delta
