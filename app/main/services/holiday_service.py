from app.main.models import Holiday

class HolidayService:
    def __init__(self):
        pass
 
    @staticmethod
    def get_all_holiday_data():
        user_entities = Holiday.query.all()
        user_entities_list = []
        
        for user in user_entities:
            user_dict = {}
            user_dict['id'] = user.id
            user_dict['worker_id'] = user.worker_id
            user_dict['status'] = user.status
            user_dict['date'] = user.date
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at
            
            user_entities_list.append(user_dict)
        return user_entities_list
    
 
    @staticmethod
    def get_holiday_by_id(id):
        user_entities = Holiday.query.filter_by(id=id)
        user_dict = {}
        for user in user_entities:
            user_dict['id'] = user.id
            user_dict['worker_id'] = user.worker_id
            user_dict['status'] = user.status
            user_dict['date'] = user.date
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at

        return user_dict


    @staticmethod
    def save_new_holiday(data):
        new_user = Holiday(
            worker_id=data["worker_id"],
            status="Pending",
            date=data["date"],
        )
        new = Holiday.create(new_user)
        response_object = {
            "status": "success",
            "object":{
                "id":new.id,
                "worker_id":new.worker_id,
                "status":new.status,
                "date":new.date,
            },
            "message": "Successfully added.",
        }
        return response_object, 201
        
    @staticmethod
    def delete_holiday(id):
        user= Holiday.query.filter_by(id=id).first()
        
        if user:
            Holiday.delete(user)
            response_object = {
                "status": "success",
                "message": "Successfully deleted.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Holiday does not exists.",
            }
            return response_object, 409
        

    @staticmethod
    def update_holiday(id,data):
        user= Holiday.query.filter_by(id=id).first()
        
        if user:
            user.status = data.get('status', user.status)
            user.date = data.get('date', user.date)

            new = Holiday.update(user)
            response_object = {
                "status": "success",
                "object":{
                    "id":new.id,
                    "worker_id":new.worker_id,
                    "status":new.status,
                    "date":new.date,
                },
                "message": "Successfully updated.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Holiday details not found.",
            }
            return response_object, 409
    
    @staticmethod
    def update_holiday_status(id):
        user= Holiday.query.filter_by(id=id).first()

        if user:
            user.status = "Completed"

            new = Holiday.update(user)
            response_object = {
                "status": "success",
                "object":{
                    "id":new.id,
                    "worker_id":new.worker_id,
                    "status":new.status,
                    "date":new.date,
                },
                "message": "Successfully updated.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Holiday details not found.",
            }
            return response_object, 409

    @staticmethod
    def get_pending_holiday_serv():
        worker_entities = Holiday.query.filter_by(status='Pending')
        worker_entities_list = []

        for user in worker_entities:
            user_dict = {}
            user_dict['id'] = user.id
            user_dict['worker_id'] = user.worker_id
            user_dict['status'] = user.status
            user_dict['date'] = user.date
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at

            worker_entities_list.append(user_dict)
        return worker_entities_list
    

    @staticmethod
    def get_Completed_holiday():
        worker_entities = Holiday.query.filter_by(status='Completed')
        worker_entities_list = []

        for user in worker_entities:
            user_dict = {}
            user_dict['id'] = user.id
            user_dict['worker_id'] = user.worker_id
            user_dict['status'] = user.status
            user_dict['date'] = user.date
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at

            worker_entities_list.append(user_dict)
        return worker_entities_list