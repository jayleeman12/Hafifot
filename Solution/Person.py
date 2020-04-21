"""Person module"""
from typing import Dict
from enum import Enum
from Hafifot.Solution.Logger import Event
from Hafifot.Solution.Error import AlreadyExistsError, NotFoundError


class Status(Enum):
    """Enum class to represent health status"""
    Healthy = 1
    Corona = 2


class Person:
    def __init__(self, person_id: int, status: Status, loc_history: Dict):
        self.person_id = person_id
        self.status = status
        self.loc_history = loc_history

    # Setters & Getters
    def get_id(self) -> int:
        return self.person_id

    def set_id(self, person_id: int):
        self.person_id = person_id

    def get_status(self) -> Status:
        return self.status

    def set_status(self, status: Status):
        self.status = status

    def get_location_history(self) -> Dict:
        return self.loc_history

    def set_location_history(self, loc_history: Dict):
        self.loc_history = loc_history


class PersonFactory:
    def __init__(self, persons: Dict):
        self.persons = persons

    def get_persons(self):
        return self.persons

    def set_persons(self, persons):
        self.persons = persons

    def add_person(self, person: Person):
        self.persons[person.get_id()] = person

    def delete_person(self, person_id: int):
        del self.persons[person_id]

    def get_person(self, person_id: int) -> Person:
        return self.persons[person_id]


class PersonController:
    """A class to preform actions on a specific Person"""

    def __init__(self, person: Person):
        self.person = person

    def add_event(self, event: Event):
        if event.get_id() in self.person.get_location_history():
            raise AlreadyExistsError("event already exists in person's details")
        self.person.loc_history[event.get_id()] = event

    def delete_event(self, event_id: int):
        if event_id not in self.person.get_location_history():
            raise NotFoundError("event not fount in person's details")
        del self.person.loc_history[event_id]
