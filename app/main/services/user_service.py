from app.main.models import User
import uuid 
from  werkzeug.security import generate_password_hash, check_password_hash


class UserService:
    def __init__(self):
        pass
 
    @staticmethod
    def get_all_user_data():
        user_entities = User.query.all()
        user_entities_list = []
        
        for user in user_entities:
            user_dict = {}
            user_dict['public_id'] = user.public_id
            user_dict['id'] = user.id
            user_dict['email'] = user.email
            user_dict['pincode'] = user.pincode
            user_dict['phone_number'] = user.phone_number
            user_dict['last_name'] = user.last_name
            user_dict['first_name'] = user.first_name
            user_dict['city'] = user.city
            user_dict['dob'] = user.dob
            user_dict['state'] = user.state
            user_dict['address'] = user.address
            user_dict['hash_password'] = user.hash_password
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at
            user_dict['role'] = user.role
            
            user_entities_list.append(user_dict)
        return user_entities_list
    
 
    @staticmethod
    def get_user_by_id(id):
        user_entities = User.query.filter_by(id=id)
        user_entities_list = []

        for user in user_entities:
            user_dict = {}
            user_dict['public_id'] = user.public_id
            user_dict['id'] = user.id
            user_dict['pincode'] = user.pincode
            user_dict['email'] = user.email
            user_dict['phone_number'] = user.phone_number
            user_dict['last_name'] = user.last_name
            user_dict['first_name'] = user.first_name
            user_dict['city'] = user.city
            user_dict['dob'] = user.dob
            user_dict['state'] = user.state
            user_dict['address'] = user.address
            user_dict['hash_password'] = user.hash_password
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at
            user_dict['role'] = user.role
            
            user_entities_list.append(user_dict)
        return user_entities_list


    @staticmethod
    def save_new_user(data):
        user = User.query.filter_by(email=data["email"], phone_number=data["phone_number"]).first()
        password=data["hash_password"]
        if not user:
            new_user = User(
                public_id = str(uuid.uuid4()),
                email=data["email"],
                phone_number=data["phone_number"],
                last_name=data["last_name"],
                first_name=data["first_name"],
                dob = data.get('dob', "-"),
                city=data["city"],
                state=data["state"],
                pincode=data["pincode"],
                address=data["address"],
                role="User",
                hash_password=generate_password_hash(password)
            )
            new = User.create(new_user)
            response_object = {
                "status": "success",
                "object":{
                    "email":new.email,
                    "phone_number":new.phone_number,
                    "last_name":new.last_name,
                    "first_name":new.first_name,
                    "city":new.city,
                    "state":new.state,
                    "dob":new.dob,
                    "address":new.address,
                    "pincode":new.pincode,
                    "hash_password":new.hash_password,
                    "id":new.id,
                    "role":new.role,
                },
                "message": "Successfully added.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Email already exists. Please use new one.",
            }
            return response_object, 409
        


    @staticmethod
    def delete_user(id):
        user= User.query.filter_by(id=id).first()
        
        if user:
            User.delete(user)
            response_object = {
                "status": "success",
                "message": "Successfully deleted.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "User does not exists.",
            }
            return response_object, 409
        

    @staticmethod
    def update_user(id,data):
        user= User.query.filter_by(id=id).first()
        
        if user:
            user.email = data.get('email', user.email)
            user.phone_number = data.get('phone_number', user.phone_number)
            user.first_name = data.get('first_name', user.first_name)
            user.last_name = data.get('last_name', user.last_name)
            user.city = data.get('city', user.city)
            user.state = data.get('state', user.state)
            user.address = data.get('address', user.address)
            user.pincode = data.get('pincode', user.pincode)
            user.dob = data.get('dob', user.dob)
            user.hash_password = generate_password_hash(data.get('hash_password', user.hash_password))
            user.role = data.get('role', user.role)

            new = User.update(user)
            response_object = {
                "status": "success",
                "object":{
                    "email":new.email,
                    "phone_number":new.phone_number,
                    "last_name":new.last_name,
                    "first_name":new.first_name,
                    "city":new.city,
                    "state":new.state,
                    "dob":new.dob,
                    "address":new.address,
                    "hash_password":new.hash_password,
                    "id":new.id,
                    "pincode":new.pincode,
                    "role":new.role,
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