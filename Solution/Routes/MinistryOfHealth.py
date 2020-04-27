"""Route layout of /moh URL, functionality for getting update and checking infected locations"""
import json

from datetime import datetime
from datetimerange import DateTimeRange
from flask import Blueprint, request
from Hafifot.Solution.Controllers.MinistryOfHealth import CoronaDept
from Hafifot.Solution.Controllers.Logger import Event


moh_route = Blueprint('moh_route', __name__)


@moh_route.route('/updates', methods=['GET'])
def get_updates():
    persons = CoronaDept.get_instance().check_for_updates()
    output = {}
    for person_id, days in persons:
        output[person_id] = json.dumps({'person_id': person_id, 'isolation_days': days})
    return json.dumps({'persons': output})


@moh_route.route('/location', methods=['GET'])
def check_location():
    req_data = request.get_json()
    event = json.loads(json.dumps(req_data))
    event = Event(-999, datetime.strptime(event['date'], '%Y-%m-%d'),
                  DateTimeRange(event['time_range'].split(' ')[0],
                                event['time_range'].split(' ')[1]),
                  event['location'])

    if CoronaDept.get_instance().check_collision(event):
        return 'If you visited there, You Better enter isolation!'
    else:
        return 'No worries, You are safe :)'
