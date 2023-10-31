from app.main.models import Booking
from app.main.services.worker_service import WorkerService
from app.main.services.user_service import UserService

class BookingService:
    def __init__(self):
        pass
 
    @staticmethod
    def get_all_booking_data():
        user_entities = Booking.query.all()
        user_entities_list = []
        
        for user in user_entities:
            user_dict = {}
            user_dict['id'] = user.id
            user_dict['user_id'] = user.user_id
            user_dict['worker_id'] = user.worker_id
            user_dict['status'] = user.status
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at
            
            user_entities_list.append(user_dict)
        return user_entities_list
    
 
    @staticmethod
    def get_booking_by_id(id):
        user_entities = Booking.query.filter_by(id=id)
        user_dict = {}
        for user in user_entities:
            user_dict['id'] = user.id
            user_dict['user_id'] = user.user_id
            user_dict['worker_id'] = user.worker_id
            user_dict['status'] = user.status
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at

        user_id = user_dict['user_id']
        worker_id = user_dict['worker_id']
        user = UserService().get_user_by_id(id=user_id)
        worker = WorkerService().get_worker_by_id(id=worker_id)
        response_object = {
            "status": "success",
            "object":{
                "user":user,
                "worker":worker
            },
            "message": "Successfully Fetched.",
        }

        return response_object


    @staticmethod
    def save_new_booking(data):
        if data["user_id"] == 2:
            response_object = {
                "status": "failed",
                "message": "Admin cannot added booking",
            }
            return response_object, 409
        new_user = Booking(
            user_id=data["user_id"],
            worker_id=data["worker_id"],
            status="Pending",
        )
        new = Booking.create(new_user)
        response_object = {
            "status": "success",
            "object":{
                "id":new.id,
                "user_id":new.user_id,
                "worker_id":new.worker_id,
                "status":new.status,
            },
            "message": "Successfully added.",
        }
        return response_object, 201
        
    @staticmethod
    def delete_booking(id):
        user= Booking.query.filter_by(id=id).first()
        
        if user:
            Booking.delete(user)
            response_object = {
                "status": "success",
                "message": "Successfully deleted.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Booking does not exists.",
            }
            return response_object, 409
        

    @staticmethod
    def update_booking(id,data):
        user= Booking.query.filter_by(id=id).first()
        
        if user:
            user.status = data.get('status', user.status)

            new = Booking.update(user)
            response_object = {
                "status": "success",
                "object":{
                    "id":new.id,
                    "user_id":new.user_id,
                    "worker_id":new.worker_id,
                    "status":new.status,
                },
                "message": "Successfully updated.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "User details not found.",
            }
            return response_object, 409
    
    @staticmethod
    def update_booking_status(id):
        user= Booking.query.filter_by(id=id).first()

        if user:
            user.status = "Completed"

            new = Booking.update(user)
            response_object = {
                "status": "success",
                "object":{
                    "id":new.id,
                    "user_id":new.user_id,
                    "worker_id":new.worker_id,
                    "status":new.status,
                },
                "message": "Successfully updated.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Booking details not found.",
            }
            return response_object, 409

    @staticmethod
    def get_pending_booking_serv():
        worker_entities = Booking.query.filter_by(status='Pending')
        worker_entities_list = []

        for user in worker_entities:
            user_dict = {}
            user_dict['id'] = user.id
            user_dict['user_id'] = user.user_id
            user_dict['worker_id'] = user.worker_id
            user_dict['status'] = user.status
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at

            worker_entities_list.append(user_dict)
        return worker_entities_list
    

    @staticmethod
    def get_Completed_booking():
        worker_entities = Booking.query.filter_by(status='Completed')
        worker_entities_list = []

        for user in worker_entities:
            user_dict = {}
            user_dict['id'] = user.id
            user_dict['user_id'] = user.user_id
            user_dict['worker_id'] = user.worker_id
            user_dict['status'] = user.status
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at

            worker_entities_list.append(user_dict)
        return worker_entities_list