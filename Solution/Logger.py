"""Logger module"""
from typing import Dict
from abc import ABC
from datetime import datetime
from datetimerange import DateTimeRange


class Event:
    def __init__(self, event_id: int, date: datetime, time_range: DateTimeRange, location: str):
        self.date = date
        self.time_range = time_range
        self.location = location
        self.event_id = event_id


class Logger(ABC):
    """Base class for this module"""

    def __init__(self, events: Dict):
        self.events = events

    def get_events(self) -> Dict:
        return self.events

    def set_events(self, events: Dict):
        self.events = events

    def get_event(self, event_id: int) -> Event:
        return self.events[event_id]

    def delete_event(self, event_id: int):
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
