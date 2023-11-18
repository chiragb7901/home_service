from flask import Blueprint, current_app,request

from app.main.services.holiday_service import HolidayService
from app.main.services.worker_service import token_required

holiday = Blueprint("holiday", __name__)


@holiday.route('/v1/holidays', methods=['GET'])
@token_required
def get_all_booking(current_user):

    user_entities = HolidayService().get_all_holiday_data()

    resp = {
        'status': True,
        'msg': 'Holidays successfully fetched',
        'data': user_entities
    }
    return resp


@holiday.route('/v1/holiday/<id>', methods=['GET'])
@token_required
def get_booking_by_id(current_user,id):

    user_entities = HolidayService().get_holiday_by_id(id=id)

    resp = {
        'status': True,
        'msg': 'Holiday successfully fetched',
        'data': user_entities
    }
    return resp

@holiday.route('/v1/holiday/pending', methods=['GET'])
@token_required
def get_pending_booking_route(current_user):

    worker_entities = HolidayService().get_pending_holiday_serv()

    resp = {
        'status': True,
        'msg': 'Holidays successfully fetched',
        'data': worker_entities
    }
    return resp


@holiday.route('/v1/holiday/completed', methods=['GET'])
@token_required
def get_Completed_booking(current_user):

    worker_entities = HolidayService().get_Completed_holiday()

    resp = {
        'status': True,
        'msg': 'Holidays successfully fetched',
        'data': worker_entities
    }
    return resp

@holiday.route('/v1/holiday/update/status/<id>', methods=['POST'])
@token_required
def update_status(current_user,id):
    worker = HolidayService().update_holiday_status(id)
    resp = {
        'status': True,
        'msg': 'Holiday details successfully fetched',
        'data': worker
    }
    return resp


@holiday.route('/v1/holidays', methods=['POST'])
def save_new_booking():
    data = request.get_json()
    user_entities = HolidayService().save_new_holiday(data)
    resp = {
        'status': True,
        'msg': 'Holiday details successfully saved',
        'data': user_entities
    }
    return resp


@holiday.route('/v1/holiday/delete/<id>', methods=['DELETE'])
@token_required
def delete_booking(current_user,id):

    user = HolidayService().delete_holiday(id)
    resp = {
        'status': True,
        'msg': 'Holiday details successfully fetched',
        'data': user
    }
    return resp


@holiday.route('/v1/holiday/update/<id>', methods=['PUT'])
@token_required
def update_booking(current_user,id):
    data = request.get_json()
    user = HolidayService().update_holiday(id,data)
    resp = {
        'status': True,
        'msg': 'Holiday details successfully fetched',
        'data': user
    }
    return resp

