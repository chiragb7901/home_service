from flask import Blueprint, current_app,request

from app.main.services.worker_service import WorkerService,token_required
from app.main.services.user_service import UserService

worker = Blueprint("worker", __name__)


@worker.route('/v1/workers', methods=['GET'])
def get_all_workers():

    worker_entities = WorkerService().get_all_worker_data()

    resp = {
        'status': True,
        'msg': 'Workers successfully fetched',
        'data': worker_entities
    }
    return resp


@worker.route('/v1/workers/pending', methods=['GET'])
@token_required
def get_pending_worker_route(current_user):

    worker_entities = WorkerService().get_pending_worker_serv()

    resp = {
        'status': True,
        'msg': 'Workers successfully fetched',
        'data': worker_entities
    }
    return resp


@worker.route('/v1/workers/completed', methods=['GET'])
@token_required
def get_Completed_worker(current_user):

    worker_entities = WorkerService().get_Completed_worker()

    resp = {
        'status': True,
        'msg': 'Workers successfully fetched',
        'data': worker_entities
    }
    return resp


@worker.route('/v1/worker/<id>', methods=['GET'])
@token_required
def get_worker_by_id(current_user,id):

    worker_entities = WorkerService().get_worker_by_id(id=id)

    resp = {
        'status': True,
        'msg': 'Worker successfully fetched',
        'data': worker_entities
    }
    return resp

@worker.route('/v1/worker/photourls', methods=['GET'])
def get_all_photo_urls():

    worker_entities = WorkerService().get_all_photourls()

    resp = {
        'status': True,
        'msg': 'Worker successfully fetched',
        'data': worker_entities
    }
    return resp

@worker.route('/v1/signup', methods=['POST'])
def save_new_worker():
    data = request.get_json()
    resp = "";
    if data["role"]=='User':
        resp = UserService().save_new_user(data)
    else:
        resp = WorkerService().save_new_worker(data)
    
    resp = {
        'status': True,
        'msg': 'Account Successfully created',
        'data': resp
    }
    return resp


@worker.route('/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    login_entity = WorkerService().login(data)
    resp = {
        'status': True,
        'data': login_entity
    }
    return resp


@worker.route('/v1/worker/delete/<id>', methods=['DELETE'])
@token_required
def delete_worker(current_user,id):

    worker = WorkerService().delete_worker(id)
    resp = {
        'status': True,
        'msg': 'Worker details successfully fetched',
        'data': worker
    }
    return resp


@worker.route('/v1/worker/update/<id>', methods=['PUT'])
@token_required
def update_worker(current_user,id):
    data = request.get_json()
    worker = WorkerService().update_worker(id,data)
    resp = {
        'status': True,
        'msg': 'Worker details successfully fetched',
        'data': worker
    }
    return resp


@worker.route('/v1/worker/update/status/<id>', methods=['POST'])
@token_required
def update_status(current_user,id):
    worker = WorkerService().update_worker_status(id)
    resp = {
        'status': True,
        'msg': 'Worker details successfully fetched',
        'data': worker
    }
    return resp

