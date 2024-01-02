import uuid
from datetime import datetime
from flask.views import MethodView
from flask_smorest import Blueprint

blueprint = Blueprint('kitchen', __name__, description='Kitchen API')

schedules = [{
    'id': str(uuid.uuid4()),
    'scheduled': datetime.now(),
    'status': 'pending',
    'order': [
        {
            'product': 'capuccino',
            'quantity': 1,
            'size': 'big'
        }
    ]
}]


@blueprint.route('/kitchen/schedules')
class KitchenSchedules(MethodView):
    def get(self):
        return {
            'schedules': schedules
        }, 200

    def post(self, payload):
        return schedules[0], 201


@blueprint.route('/kitchen/schedules/<schedule_id>')
class KitchenSchedule(MethodView):
    def get(self, schedule_id):
        return schedules[0], 200

    def put(self, payload, schedule_id):
        return schedules[0], 200

    def delete(self, schedule_id):
        return '', 204


@blueprint.route('/kitchen/schedules/<schedule_id>/cancel', methods=['POST'])
def cancel_schedule(schedule_id):
    return schedules[0], 200


@blueprint.route('/kitchen/schedules/<schedule_id>/status', methods=['GET'])
def get_schedule_status(schedule_id):
    return schedules[0], 200
