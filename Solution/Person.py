"""Person module"""
from typing import Dict


class Person:
    def __init__(self, taz, status, loc_history):
        self.id = taz
        self.status = status
        self.loc_history = loc_history

    # Setters & Getters
    def get_id(self):
        return self.id

    def set_id(self, taz):
        self.id = taz

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_location_history(self):
        return self.loc_history

    def set_location_history(self, loc_history):
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

    def delete_person(self, taz: int):
        del self.persons[taz]
