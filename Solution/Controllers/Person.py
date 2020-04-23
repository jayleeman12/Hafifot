"""Person module"""
import json
from typing import Dict
from enum import Enum
from Hafifot.Solution.Controllers.Logger import Event
from Hafifot.Solution.Controllers.Error import AlreadyExistsError, NotFoundError


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
        if person.get_id() in self.persons:
            raise AlreadyExistsError(f'person ID: {person.get_id()} already exists in the factory')
        self.persons[person.get_id()] = person

    def delete_person(self, person_id: int):
        if person_id not in self.persons:
            raise NotFoundError(f'person ID: {person_id} not found in the factory')
        del self.persons[person_id]

    def get_person(self, person_id: int) -> Person:
        if person_id not in self.persons:
            raise NotFoundError(f'person ID: {person_id} not found in the factory')
        return self.persons[person_id]

    def create_person(self, person_id: int, status: Status, loc_history: Dict) -> Person:
        if person_id in self.persons:
            raise AlreadyExistsError(f'person ID: {person_id} already exists in the factory')
        return Person(person_id, status, loc_history)

    def persons_to_json(self):
        output = {}
        for person in self.persons.values():
            output[person.get_id()] = json.loads(PersonController.person_to_json(person))
        return json.dumps({'persons': output})

    def person_to_json(self, person_id: int):
        person = self.get_person(person_id)
        return PersonController.person_to_json(person)

    def update_person(self, person_id: int, status: Status, loc_history: Dict) -> Person:
        if person_id not in self.persons:
            raise NotFoundError(f'person ID: {person_id} not found in the factory')
        self.persons[person_id].set_status(status)
        self.persons[person_id].set_location_history(loc_history)
        return self.persons[person_id]


class PersonController:
    """A class to preform actions on a specific Person"""

    @staticmethod
    def add_event(person: Person, event: Event):
        if event.get_id() in person.get_location_history():
            raise AlreadyExistsError("event already exists in person's details")
        person.loc_history[event.get_id()] = event

    @staticmethod
    def delete_event(person: Person, event_id: int):
        if event_id not in person.get_location_history():
            raise NotFoundError("event not found in person's details")
        del person.loc_history[event_id]

    @staticmethod
    def person_to_json(person: Person):
        json_person = {'person_id': person.get_id(), 'status': person.get_status(),
                       'loc_history': person.get_location_history()}
        return json.dumps(json_person)

