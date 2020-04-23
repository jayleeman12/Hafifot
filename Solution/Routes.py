import json
from flask import Flask, request
from Hafifot.Solution.Person import PersonFactory, PersonController
from Hafifot.Solution.Logger import CoronaLogger
from Hafifot.Solution.Error import AlreadyExistsError, NotFoundError


app = Flask(__name__)


@app.route('/factory/persons', methods=['POST'])
def create_person():
    req_data = request.get_json()
    person = json.loads(json.dumps(req_data))
    try:
        person = factory.create_person(person['person_id'], person['status'], person['loc_history'])
        factory.add_person(person)

    except AlreadyExistsError as e:
        return e.message

    return PersonController.person_to_json(factory.get_person(person.get_id()))


@app.route('/factory/persons', methods=['GET'])
def get_persons():
    return factory.persons_to_json()


@app.route('/factory/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    try:
        factory.delete_person(person_id)
        return json.dumps(f'Person with ID: {person_id} deleted successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@app.route('/factory/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    req_data = request.get_json()
    person = json.loads(json.dumps(req_data))
    try:
        person = factory.update_person(person_id, person['status'], person['loc_history'])
        return json.dumps(f'Person with ID: {person_id} updated successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@app.route('/factory/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    try:
        return PersonController.person_to_json(factory.get_person(person_id))

    except NotFoundError as e:
        return json.dumps(e.message)


if __name__ == '__main__':
    factory = PersonFactory({})
    logger = CoronaLogger({}, 14)
    app.run(debug=True, port=5000)
