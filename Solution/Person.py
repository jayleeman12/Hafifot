"""Person module"""
from typing import Dict
from enum import Enum


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
    def get_person_id(self) -> int:
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
        self.persons[person.get_person_id()] = person

    def delete_person(self, person_id: int):
        del self.persons[person_id]
