"""Route layout of /events URL, CRUD functionality for corona events"""

import json
from flask import Blueprint, request
from Hafifot.Solution.Sever import *
from Hafifot.Solution.Controllers.Logger import CoronaLogger, CoronaController
from Hafifot.Solution.Controllers.Error import AlreadyExistsError, NotFoundError


events_route = Blueprint('events_route', __name__)


@events_route.route('/events', methods=['POST'])
def create_event():
    req_data = request.get_json()
    event = json.loads(json.dumps(req_data))
    try:
        event = corona_dept.create_event(event['event_id'], event['date'],
                                         event['time_range'],
                                         event['location'])
        corona_dept.add_event(event)

    except AlreadyExistsError as e:
        return e.message

    return CoronaController.event_to_json(corona_dept.get_logger().get_event(event.get_id()))


@events_route.route('/events', methods=['GET'])
def get_events():
    return corona_dept.events_to_json()


@events_route.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        corona_dept.delete_event(event_id)
        return json.dumps(f'Event with ID: {event_id} deleted successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@events_route.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    req_data = request.get_json()
    event = json.loads(json.dumps(req_data))
    try:
        event = corona_dept.update_event(event_id, event['date'], event['time_range'], event['location'])
        return json.dumps(f'Event with ID: {event_id} updated successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@events_route.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    try:
        return CoronaController.event_to_json(corona_dept.get_event(event_id))

    except NotFoundError as e:
        return json.dumps(e.message)
