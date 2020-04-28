"""Route layout of /factory URL, CRUD functionality for persons in the factory"""

import json
from datetime import datetime
from datetimerange import DateTimeRange
from flask import Blueprint, request
from Hafifot.Solution.Controllers.MinistryOfHealth import CoronaDept
from Hafifot.Solution.Controllers.Person import PersonController, Status
from Hafifot.Solution.Controllers.Error import AlreadyExistsError, NotFoundError


factory_route = Blueprint('factory_route', __name__)


@factory_route.route('/persons', methods=['POST'])
def create_person():
    req_data = request.get_json()
    person = json.loads(json.dumps(req_data))
    loc_history = parse_location_history(person['loc_history'])
    try:
        person = CoronaDept.get_instance().create_person(person['person_id'], Status(person['status']), loc_history)
        CoronaDept.get_instance().add_person(person)

    except AlreadyExistsError as e:
        return e.message

    return PersonController.person_to_json(CoronaDept.get_instance().get_person(person.get_id()))


@factory_route.route('/persons', methods=['GET'])
def get_persons():
    return PersonController.persons_to_json(CoronaDept.get_instance().get_factory())


@factory_route.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    try:
        CoronaDept.get_instance().delete_person(person_id)
        return json.dumps(f'Person with ID: {person_id} deleted successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@factory_route.route('/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    req_data = request.get_json()
    person = json.loads(json.dumps(req_data))
    try:
        person = CoronaDept.get_instance().update_person(person_id, Status(person['status']), person['loc_history'])
        return json.dumps(f'Person with ID: {person_id} updated successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@factory_route.route('/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    try:
        return PersonController.person_to_json(CoronaDept.get_instance().get_person(person_id))

    except NotFoundError as e:
        return json.dumps(e.message)


def parse_location_history(json_loc_history: dict) -> dict:
    loc_history = {}
    for item in json_loc_history.values():
        loc_history[int(item['event_id'])] = \
            CoronaDept.get_instance().create_event(int(item['event_id']),
                                                   datetime.strptime(item['date'], '%Y-%m-%d'),
                                                   DateTimeRange(item['time_range'].split(' ')[0],
                                                   item['time_range'].split(' ')[1]),
                                                   item['location'])

    return loc_history
