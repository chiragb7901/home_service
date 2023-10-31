from flask import Blueprint, current_app,request

from app.main.services.booking_service import BookingService
from app.main.services.worker_service import token_required

booking = Blueprint("booking", __name__)


@booking.route('/v1/bookings', methods=['GET'])
@token_required
def get_all_booking(current_user):

    user_entities = BookingService().get_all_booking_data()

    resp = {
        'status': True,
        'msg': 'Bookings successfully fetched',
        'data': user_entities
    }
    return resp


@booking.route('/v1/booking/<id>', methods=['GET'])
@token_required
def get_booking_by_id(current_user,id):

    user_entities = BookingService().get_booking_by_id(id=id)

    resp = {
        'status': True,
        'msg': 'Booking successfully fetched',
        'data': user_entities
    }
    return resp

@booking.route('/v1/booking/pending', methods=['GET'])
@token_required
def get_pending_booking_route(current_user):

    worker_entities = BookingService().get_pending_booking_serv()

    resp = {
        'status': True,
        'msg': 'Bookings successfully fetched',
        'data': worker_entities
    }
    return resp


@booking.route('/v1/booking/completed', methods=['GET'])
@token_required
def get_Completed_booking(current_user):

    worker_entities = BookingService().get_Completed_booking()

    resp = {
        'status': True,
        'msg': 'Bookings successfully fetched',
        'data': worker_entities
    }
    return resp

@booking.route('/v1/booking/update/status/<id>', methods=['POST'])
@token_required
def update_status(current_user,id):
    worker = BookingService().update_booking_status(id)
    resp = {
        'status': True,
        'msg': 'Booking details successfully fetched',
        'data': worker
    }
    return resp


@booking.route('/v1/bookings', methods=['POST'])
def save_new_booking():
    data = request.get_json()
    user_entities = BookingService().save_new_booking(data)
    resp = {
        'status': True,
        'msg': 'Booking details successfully saved',
        'data': user_entities
    }
    return resp


@booking.route('/v1/booking/delete/<id>', methods=['DELETE'])
@token_required
def delete_booking(current_user,id):

    user = BookingService().delete_booking(id)
    resp = {
        'status': True,
        'msg': 'User details successfully fetched',
        'data': user
    }
    return resp


@booking.route('/v1/booking/update/<id>', methods=['PUT'])
@token_required
def update_booking(current_user,id):
    data = request.get_json()
    user = BookingService().update_booking(id,data)
    resp = {
        'status': True,
        'msg': 'Booking details successfully fetched',
        'data': user
    }
    return resp

