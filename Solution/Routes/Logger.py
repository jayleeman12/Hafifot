"""Route layout of /events URL, CRUD functionality for corona events"""

import json
from datetime import datetime
from datetimerange import DateTimeRange
from flask import Blueprint, request
from Hafifot.Solution.Controllers.MinistryOfHealth import CoronaDept
from Hafifot.Solution.Controllers.Logger import CoronaController
from Hafifot.Solution.Controllers.Error import AlreadyExistsError, NotFoundError


events_route = Blueprint('events_route', __name__)


@events_route.route('/events', methods=['POST'])
def create_event():
    req_data = request.get_json()
    event = json.loads(json.dumps(req_data))
    try:
        event = CoronaDept.get_instance().create_event(event['event_id'],
                                                       datetime.strptime(event['date'], '%Y-%m-%d'),
                                                       DateTimeRange(event['time_range'].split(' ')[0],
                                                                     event['time_range'].split(' ')[1]),
                                                       event['location'])
        CoronaDept.get_instance().add_event(event)

    except AlreadyExistsError as e:
        return e.message

    return CoronaController.event_to_json(CoronaDept.get_instance().get_logger().get_event(event.get_id()))


@events_route.route('/events', methods=['GET'])
def get_events():
    return CoronaDept.get_instance().events_to_json()


@events_route.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        CoronaDept.get_instance().delete_event(event_id)
        return json.dumps(f'Event with ID: {event_id} deleted successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@events_route.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    req_data = request.get_json()
    event = json.loads(json.dumps(req_data))
    try:
        event = CoronaDept.get_instance().update_event(event_id, datetime.strptime(event['date'], '%Y-%m-%d'),
                                                       DateTimeRange(event['time_range'].split(' ')[0],
                                                                     event['time_range'].split(' ')[1]),
                                                       event['location'])
        return json.dumps(f'Event with ID: {event_id} updated successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@events_route.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    try:
        return CoronaController.event_to_json(CoronaDept.get_instance().get_event(event_id))

    except NotFoundError as e:
        return json.dumps(e.message)
