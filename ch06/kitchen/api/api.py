import copy
import uuid
from datetime import datetime
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from api.schemas import (
    GetScheduledOrderSchema,
    ScheduleOrderSchema,
    GetScheduledOrdersSchema,
    ScheduleStatusSchema,
    GetKitchenScheduleParameters
)
from marshmallow import ValidationError

blueprint = Blueprint('kitchen', __name__, description='Kitchen API')

# schedules = [{
#     'id': str(uuid.uuid4()),
#     'scheduled': datetime.now(),
#     'status': 'pending',
#     'order': [
#         {
#             'product': 'capuccino',
#             'quantity': 1,
#             'size': 'big'
#         }
#     ]
# }]
schedules = []


def validate_schedule(schedule):
    schedule = copy.deepcopy(schedule)
    schedule['scheduled'] = schedule['scheduled'].isoformat()
    errors = GetScheduledOrderSchema().validate(schedule)
    if errors:
        raise ValidationError(errors)


@blueprint.route('/kitchen/schedules')
class KitchenSchedules(MethodView):
    @blueprint.arguments(GetKitchenScheduleParameters, location='query')
    @blueprint.response(status_code=200, schema=GetScheduledOrdersSchema)
    def get(self, parameters):
        # データを検証
        for schedule in schedules:
            validate_schedule(schedule)
            schedule = copy.deepcopy(schedule)
            schedule['scheduled'] = schedule['scheduled'].isoformat()
            errors = GetScheduledOrderSchema().validate(schedule)
            if errors:
                raise ValidationError(errors)

        # no parameters
        if not parameters:
            return {'schedules': schedules}

        query_set = [schedules for schedule in schedules]
        in_progress = parameters.get('progress')
        if in_progress is not None:
            if in_progress:
                query_set = [
                    schedule for schedule in schedules
                    if schedule['status'] == 'progress'
                ]
            else:
                query_set = [
                    schedule for schedule in schedules
                    if schedule['status'] != 'progress'
                ]

        since = parameters.get('since')
        if since is not None:
            query_set = [
                schedule for schedule in schedules
                if schedule['scheduled'] >= since
            ]

        limit = parameters.get('limit')
        if limit is not None and len(query_set) > limit:
            query_set = query_set[:limit]
        return {'schedules': query_set}

    @blueprint.arguments(ScheduleOrderSchema)
    @blueprint.response(status_code=201, schema=GetScheduledOrderSchema)
    def post(self, payload):
        payload['id'] = str(uuid.uuid4())
        payload['scheduled'] = datetime.utcnow()
        payload['status'] = 'pending'
        schedules.append(payload)
        validate_schedule(payload)
        return payload


@blueprint.route('/kitchen/schedules/<schedule_id>')
class KitchenSchedule(MethodView):
    @blueprint.response(status_code=200, schema=GetScheduledOrderSchema)
    def get(self, schedule_id):
        return schedules[0]

    @blueprint.arguments(ScheduleOrderSchema)
    @blueprint.response(status_code=200, schema=GetScheduledOrderSchema)
    def put(self, payload, schedule_id):
        return schedules[0]

    @blueprint.response(status_code=204)
    def delete(self, schedule_id):
        return


@blueprint.response(status_code=200, schema=GetScheduledOrderSchema)
@blueprint.route('/kitchen/schedules/<schedule_id>/cancel', methods=['POST'])
def cancel_schedule(schedule_id):
    return schedules[0]


@blueprint.response(status_code=200, schema=ScheduleStatusSchema)
@blueprint.route('/kitchen/schedules/<schedule_id>/status', methods=['GET'])
def get_schedule_status(schedule_id):
    return schedules[0]
