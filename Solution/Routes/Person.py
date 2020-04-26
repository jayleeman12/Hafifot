"""Route layout of /factory URL, CRUD functionality for persons in the factory"""

import json
from flask import Blueprint, request
from Hafifot.Solution.Sever import *
from Hafifot.Solution.Controllers.Person import PersonFactory, PersonController
from Hafifot.Solution.Controllers.Error import AlreadyExistsError, NotFoundError


factory_route = Blueprint('factory_route', __name__)


@factory_route.route('/persons', methods=['POST'])
def create_person():
    req_data = request.get_json()
    person = json.loads(json.dumps(req_data))
    try:
        person = corona_dept.create_person(person['person_id'], person['status'], person['loc_history'])
        corona_dept.add_person(person)

    except AlreadyExistsError as e:
        return e.message

    return PersonController.person_to_json(factory.get_person(person.get_id()))


@factory_route.route('/persons', methods=['GET'])
def get_persons():
    return corona_dept.persons_to_json()


@factory_route.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    try:
        corona_dept.delete_person(person_id)
        return json.dumps(f'Person with ID: {person_id} deleted successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@factory_route.route('/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    req_data = request.get_json()
    person = json.loads(json.dumps(req_data))
    try:
        person = corona_dept.update_person(person_id, person['status'], person['loc_history'])
        return json.dumps(f'Person with ID: {person_id} updated successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@factory_route.route('/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    try:
        return PersonController.person_to_json(corona_dept.get_person(person_id))

    except NotFoundError as e:
        return json.dumps(e.message)
