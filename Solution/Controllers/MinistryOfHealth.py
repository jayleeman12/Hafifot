"""Ministry Of Health module"""
import json
from abc import ABC
from datetime import datetime
from datetimerange import DateTimeRange
from Hafifot.Solution.Controllers.Person import PersonFactory,PersonController, Person, Status
from Hafifot.Solution.Controllers.Logger import CoronaLogger,CoronaController, Event


class MinistryOfHealth(ABC):
    """An abstract class"""
    def __init__(self):
        pass


class CoronaDept(MinistryOfHealth):
    """A Singleton class to wrap the factory and the logger instances and functionality"""

    instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if CoronaDept.instance is None:
            CoronaDept()
        return CoronaDept.instance

    def __init__(self):
        """ Virtually private constructor. """
        if CoronaDept.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            super().__init__()
            CoronaDept.factory = PersonFactory({})
            CoronaDept.logger = CoronaLogger({}, 14)
            CoronaDept.instance = self

    def get_factory(self) -> PersonFactory:
        return self.factory

    def set_factory(self, factory: PersonFactory):
        self.factory = factory

    def get_logger(self) -> CoronaLogger:
        return self.logger

    def set_logger(self, logger: CoronaLogger):
        self.logger = logger

    def get_persons(self):
        return self.factory.get_persons()

    def set_persons(self, persons):
        self.factory.set_persons(persons)

    # Add a person to the factory, if infected, add the location history to the logger
    def add_person(self, person: Person):
        self.factory.add_person(person)
        if person.status == 'Corona':
            CoronaController.add_infected_record(self.logger, person.loc_history)

    def delete_person(self, person_id: int):
        self.factory.delete_person(person_id)

    def get_person(self, person_id: int) -> Person:
        return self.factory.get_person(person_id)

    def create_person(self, person_id: int, status: Status, loc_history: dict) -> Person:
        return self.factory.create_person(person_id, status, loc_history)

    def persons_to_json(self) -> json:
        return self.factory.persons_to_json()

    def person_to_json(self, person_id: int):
        return self.factory.person_to_json(person_id)

    def update_person(self, person_id: int, status: Status, loc_history: dict) -> Person:
        return self.factory.update_person(person_id, status, loc_history)

    def get_events(self) -> dict:
        return self.logger.get_events()

    def set_events(self, events: dict):
        self.logger.set_events(events)

    def add_event(self, event: Event):
        self.logger.add_event(event)

    def delete_event(self, event_id: int):
        self.logger.delete_event(event_id)

    def create_event(self, event_id: int, date: datetime.date, time_range: DateTimeRange, location: str) -> Event:
        return self.logger.create_event(event_id, date, time_range, location)

    def update_event(self, event_id: int, date: datetime.date, time_range: DateTimeRange, location: str) -> Event:
        return self.logger.update_event(event_id, date, time_range, location)

    def get_event(self, event_id: int) -> Event:
        return self.logger.get_event(event_id)

    def events_to_json(self) -> json:
        return self.logger.events_to_json()

    def event_to_json(self, event_id) -> json:
        return self.logger.events_to_json(event_id)

    # For a casual (not recorded) event check if isolation needed
    # In other words, check if the time and location are infected
    def check_collision(self, event: Event) -> bool:
        return CoronaController.is_infected(self.logger, event)

    # Check for every person if he should enter isolation
    # Returns a dict of people that need isolation and for how many days
    def check_for_updates(self) -> dict:
        updates = {}
        for person_id, person in self.factory.get_persons():
            if CoronaController.enter_isolation(self.logger, person) > 0:
                updates[person_id] = CoronaController.enter_isolation(self.logger, person)

        return updates

