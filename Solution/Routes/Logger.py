import json
from flask import Flask, request
from Hafifot.Solution.Controllers.Logger import CoronaLogger, CoronaController
from Hafifot.Solution.Controllers.Error import AlreadyExistsError, NotFoundError


app = Flask(__name__)


@app.route('/logger/events', methods=['POST'])
def create_event():
    req_data = request.get_json()
    event = json.loads(json.dumps(req_data))
    try:
        event = logger.create_event(event['event_id'], event['date'], event['date'],
                                    event['time_range'], event['location'])
        logger.add_event(event)

    except AlreadyExistsError as e:
        return e.message

    return CoronaController.event_to_json(logger.get_event(event.get_id()))


@app.route('/logger/events', methods=['GET'])
def get_events():
    return logger.events_to_json()


@app.route('/logger/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        logger.delete_event(event_id)
        return json.dumps(f'Event with ID: {event_id} deleted successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@app.route('/logger/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    req_data = request.get_json()
    event = json.loads(json.dumps(req_data))
    try:
        event = logger.update_event(event_id, event['date'], event['time_range'], event['location'])
        return json.dumps(f'Event with ID: {event_id} updated successfully')

    except NotFoundError as e:
        return json.dumps(e.message)


@app.route('/logger/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    try:
        return CoronaController.event_to_json(factory.get_event(event_id))

    except NotFoundError as e:
        return json.dumps(e.message)


if __name__ == '__main__':
    logger = CoronaLogger({}, 14)
    app.run(debug=True, port=5000)

