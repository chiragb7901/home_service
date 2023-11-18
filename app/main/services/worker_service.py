from app.main.models import Worker
from app.main.models import User
import uuid
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask import request,jsonify
from app.main.settings import Config

class WorkerService:
    def __init__(self):
        pass

    @staticmethod
    def get_all_worker_data():
        worker_entities = Worker.query.all()
        worker_entities_list = []

        for user in worker_entities:
            user_dict = {}
            user_dict['public_id'] = user.public_id
            user_dict['id'] = user.id
            # user_dict['photo_urls'] = user.photo_urls
            user_dict['photo_urls'] = user.get_photo_urls(user.photo_urls)
            user_dict['email'] = user.email
            user_dict['dob'] = user.dob
            user_dict['phone_number'] = user.phone_number
            user_dict['last_name'] = user.last_name
            user_dict['first_name'] = user.first_name
            user_dict['aadhar_number'] = user.aadhar_number
            user_dict['city'] = user.city
            user_dict['state'] = user.state
            user_dict['address'] = user.address
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at
            user_dict['bank_acc_no'] = user.bank_acc_no
            user_dict['gender'] = user.gender
            user_dict['hash_password'] = user.hash_password
            user_dict['available_Days'] = user.available_Days
            user_dict['available_Hours'] = user.available_Hours
            user_dict['preferred_work'] = user.preferred_work
            user_dict['type_of_work'] = user.type_of_work
            user_dict['salary'] = user.salary
            user_dict['pincode'] = user.pincode
            user_dict['status'] = user.status

            worker_entities_list.append(user_dict)
        return worker_entities_list


    @staticmethod
    def get_worker_by_id(id):
        worker_entities = Worker.query.filter_by(id=id)
        worker_entities_list = []

        for user in worker_entities:
            user_dict = {}
            user_dict['public_id'] = user.public_id
            user_dict['id'] = user.id
            # user_dict['photo_urls'] = user.photo_urls
            user_dict['photo_urls'] = user.get_photo_urls(user.photo_urls)
            user_dict['email'] = user.email
            user_dict['phone_number'] = user.phone_number
            user_dict['dob'] = user.dob
            user_dict['last_name'] = user.last_name
            user_dict['first_name'] = user.first_name
            user_dict['aadhar_number'] = user.aadhar_number
            user_dict['city'] = user.city
            user_dict['state'] = user.state
            user_dict['address'] = user.address
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at
            user_dict['bank_acc_no'] = user.bank_acc_no
            user_dict['gender'] = user.gender
            user_dict['hash_password'] = user.hash_password
            user_dict['available_Days'] = user.available_Days
            user_dict['available_Hours'] = user.available_Hours
            user_dict['preferred_work'] = user.preferred_work
            user_dict['type_of_work'] = user.type_of_work
            user_dict['salary'] = user.salary
            user_dict['pincode'] = user.pincode
            user_dict['status'] = user.status

            worker_entities_list.append(user_dict)
        return worker_entities_list
    

    @staticmethod
    def get_pending_worker_serv():
        worker_entities = Worker.query.filter_by(status='Pending')
        worker_entities_list = []

        for user in worker_entities:
            user_dict = {}
            user_dict['public_id'] = user.public_id
            user_dict['id'] = user.id
            user_dict['email'] = user.email
            user_dict['photo_urls'] = user.get_photo_urls(user.photo_urls)
            user_dict['phone_number'] = user.phone_number
            user_dict['last_name'] = user.last_name
            user_dict['first_name'] = user.first_name
            user_dict['aadhar_number'] = user.aadhar_number
            user_dict['dob'] = user.dob
            user_dict['city'] = user.city
            user_dict['state'] = user.state
            user_dict['address'] = user.address
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at
            user_dict['bank_acc_no'] = user.bank_acc_no
            user_dict['gender'] = user.gender
            user_dict['hash_password'] = user.hash_password
            user_dict['available_Days'] = user.available_Days
            user_dict['available_Hours'] = user.available_Hours
            user_dict['preferred_work'] = user.preferred_work
            user_dict['type_of_work'] = user.type_of_work
            user_dict['salary'] = user.salary
            user_dict['pincode'] = user.pincode
            user_dict['status'] = user.status

            worker_entities_list.append(user_dict)
        return worker_entities_list
    

    @staticmethod
    def get_Completed_worker():
        worker_entities = Worker.query.filter_by(status='Completed')
        worker_entities_list = []

        for user in worker_entities:
            user_dict = {}
            user_dict['public_id'] = user.public_id
            user_dict['id'] = user.id
            user_dict['email'] = user.email
            user_dict['phone_number'] = user.phone_number
            user_dict['last_name'] = user.last_name
            user_dict['first_name'] = user.first_name
            user_dict['aadhar_number'] = user.aadhar_number
            user_dict['photo_urls'] = user.get_photo_urls(user.photo_urls)
            user_dict['city'] = user.city
            user_dict['state'] = user.state
            user_dict['address'] = user.address
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at
            user_dict['bank_acc_no'] = user.bank_acc_no
            user_dict['gender'] = user.gender
            user_dict['hash_password'] = user.hash_password
            user_dict['available_Days'] = user.available_Days
            user_dict['dob'] = user.dob
            user_dict['available_Hours'] = user.available_Hours
            user_dict['preferred_work'] = user.preferred_work
            user_dict['type_of_work'] = user.type_of_work
            user_dict['salary'] = user.salary
            user_dict['pincode'] = user.pincode
            user_dict['status'] = user.status

            worker_entities_list.append(user_dict)
        return worker_entities_list
    

    @staticmethod
    def get_all_photourls():
        worker_entities = Worker.query.all()
        worker_entities_list = []

        for user in worker_entities:
            worker_entities_list.append(user.get_photo_urls(user.photo_urls))
        
        merged_list = []
        
        for sublist in worker_entities_list:
            merged_list.extend(sublist)
        return merged_list

    @staticmethod
    def save_new_worker(data):
        if 'test@gmail.com'==data["email"]:
            response_object = {
                "status": "fail",
                "message": "Email or Phone Number already exists. Please use new one.",
            }
            return response_object, 409
        worker = Worker.query.filter_by(email=data["email"], phone_number=data["phone_number"]).first()
        password=data["hash_password"]
        if not worker:
            new_worker = Worker(
                public_id = str(uuid.uuid4()),
                email=data["email"],
                phone_number=data["phone_number"],
                last_name=data["last_name"],
                photo_urls=data["photo_urls"],
                first_name=data["first_name"],
                dob=data["dob"],
                aadhar_number=data["aadhar_number"],
                city=data["city"],
                state=data["state"],
                pincode=data["pincode"],
                status="Pending",
                address=data["address"],
                bank_acc_no=data["bank_acc_no"],
                gender=data["gender"],
                available_Days=data["available_Days"],
                available_Hours=data["available_Hours"],
                preferred_work=data["preferred_work"],
                type_of_work=data["type_of_work"],
                salary=data["salary"],
                hash_password=generate_password_hash(password)
            )
            new = Worker.create(new_worker)
            response_object = {
                "status": "success",
                "object":{
                    "email":new.email,
                    "phone_number":new.phone_number,
                    "last_name":new.last_name,
                    "first_name":new.first_name,
                    "aadhar_number":new.aadhar_number,
                    "city":new.city,
                    "state":new.state,
                    "pincode":new.pincode,
                    "status":new.status,
                    "dob":new.dob,
                    "address":new.address,
                    "bank_acc_no":new.bank_acc_no,
                    "photo_urls":new.photo_urls,
                    "gender":new.gender,
                    "available_Days":new.available_Days,
                    "available_Hours":new.available_Hours,
                    "preferred_work":new.preferred_work,
                    "type_of_work":new.type_of_work,
                    "salary":new.salary,
                    "hash_password":new.hash_password,
                    "id":new.id,
                },
                "message": "Successfully added.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Email or Phone Number already exists. Please use new one.",
            }
            return response_object, 409


    
    def convert_photo_urls(photo_urls_json):
        return json.loads(photo_urls_json) if photo_urls_json else []

    @staticmethod
    def delete_worker(id):
        worker= Worker.query.filter_by(id=id).first()

        if worker:
            Worker.delete(worker)
            response_object = {
                "status": "success",
                "message": "Successfully deleted.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Worker does not exists.",
            }
            return response_object, 409


    @staticmethod
    def update_worker(id,data):
        user= Worker.query.filter_by(id=id).first()

        if user:
            user.email = data.get('email', user.email)
            user.phone_number = data.get('phone_number', user.phone_number)
            user.first_name = data.get('first_name', user.first_name)
            user.last_name = data.get('last_name', user.last_name)
            user.aadhar_number = data.get('aadhar_number', user.aadhar_number)
            user.city = data.get('city', user.city)
            user.state = data.get('state', user.state)
            user.dob = data.get('dob', user.dob)
            user.pincode = data.get('pincode', user.pincode)
            user.status = data.get('status', user.status)
            user.address = data.get('address', user.address)
            user.bank_acc_no = data.get('bank_acc_no', user.bank_acc_no)
            user.gender = data.get('gender', user.gender)
            user.available_Days = data.get('available_Days', user.available_Days)
            user.available_Hours = data.get('available_Hours', user.available_Hours)
            user.preferred_work = data.get('preferred_work', user.preferred_work)
            user.type_of_work = data.get('type_of_work', user.type_of_work)
            user.salary = data.get('salary', user.salary)
            user.hash_password = generate_password_hash(data.get('hash_password', user.hash_password))



            new = Worker.update(user)
            response_object = {
                "status": "success",
                "object":{
                    "email":new.email,
                    "phone_number":new.phone_number,
                    "last_name":new.last_name,
                    "first_name":new.first_name,
                    "aadhar_number":new.aadhar_number,
                    "city":new.city,
                    "status":new.status,
                    "pincode":new.pincode,
                    "state":new.state,
                    "address":new.address,
                    "bank_acc_no":new.bank_acc_no,
                    "gender":new.gender,
                    "available_Days":new.available_Days,
                    "available_Hours":new.available_Hours,
                    "preferred_work":new.preferred_work,
                    "type_of_work":new.type_of_work,
                    "salary":new.salary,
                    "hash_password":new.hash_password,
                    "photo_urls":new.photo_urls,
                    "dob":new.dob,
                    "id":new.id,

                },
                "message": "Successfully updated.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Worker details not found.",
            }
            return response_object, 409
        

    @staticmethod
    def update_worker_status(id):
        user= Worker.query.filter_by(id=id).first()

        if user:
            user.status = "Completed"

            new = Worker.update(user)
            response_object = {
                "status": "success",
                "object":{
                    "email":new.email,
                    "phone_number":new.phone_number,
                    "last_name":new.last_name,
                    "first_name":new.first_name,
                    "aadhar_number":new.aadhar_number,
                    "city":new.city,
                    "status":new.status,
                    "dob":new.dob,
                    "pincode":new.pincode,
                    "state":new.state,
                    "address":new.address,
                    "bank_acc_no":new.bank_acc_no,
                    "gender":new.gender,
                    "available_Days":new.available_Days,
                    "available_Hours":new.available_Hours,
                    "preferred_work":new.preferred_work,
                    "type_of_work":new.type_of_work,
                    "photo_urls":new.photo_urls,
                    "salary":new.salary,
                    "hash_password":new.hash_password,
                    "id":new.id,

                },
                "message": "Successfully updated.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Worker details not found.",
            }
            return response_object, 409

    @staticmethod
    def login(auth):

        if not auth or not auth.get('email') or not auth.get('hash_password'):
            response_object = {
                "test":"details not found",
                "status": "fail",
                "message": 'Could not verify',
                "status_code":401,
                'WWW-Authenticate' : 'Basic realm ="Login required !!"'
            }
            return response_object
        user = None
        role = "Worker"
        user = Worker.query.filter_by(email = auth.get('email'))\
            .first()
        if user is None:
            user = User.query.filter_by(email = auth.get('email'))\
            .first()
            if user is None:
                role = "No User"
            else:
                role=user.role

        if not user:
            response_object = {
                "test":"user not found",
                "status": "fail",
                "message": 'Could not verify',
                "status_code":401,
                'WWW-Authenticate' : 'Basic realm ="Login required !!"'
            }
            return response_object

        if check_password_hash(user.hash_password,auth.get('hash_password')):

            token = jwt.encode({
                'public_id': user.public_id,
                'exp' : datetime.utcnow() + timedelta(minutes = 120)
            }, Config.SECRET_KEY)

            response_object = {
                'id':user.id,
                'token' : token,
                'role': role,
                'first_name':user.first_name,
                'last_name':user.last_name
            }
            return response_object

        else:
            response_object= {
                'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"',
                "status_code":403,
                'msg':"InCorrect Password"
                }
            return response_object




def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            current_user = Worker.query\
                .filter_by(public_id = data['public_id'])\
                .first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        return  f(current_user, *args, **kwargs)

    return decorated