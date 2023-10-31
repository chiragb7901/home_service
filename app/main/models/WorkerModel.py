from app.main import db
from datetime import datetime
import json

class Worker(db.Model):

    __tablename__ = 'worker'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    aadhar_number = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    pincode = db.Column(db.String(50))
    dob = db.Column(db.String(50))
    address = db.Column(db.String(255))
    status = db.Column(db.String(50))
    created_at =  db.Column(db.DateTime, default=datetime.utcnow,nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=False)
    bank_acc_no = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    hash_password = db.Column(db.String(255), nullable=False)
    available_Days = db.Column(db.Integer, nullable=False)
    available_Hours = db.Column(db.Integer, nullable=False)
    preferred_work = db.Column(db.String(100), nullable=False)
    type_of_work = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    photo_urls = db.Column(db.String(5000))

    def create(self):
       db.session.add(self)
       db.session.commit()
       return self
    
    def update(self):
       db.session.add(self)
       db.session.commit()
       return self
    

    def delete(self):
       db.session.delete(self)
       db.session.commit()
       return self

    def __init__(self,dob ,email, photo_urls,public_id, phone_number, first_name, last_name, city, state, address, hash_password, aadhar_number, bank_acc_no, gender, available_Days, available_Hours, preferred_work, type_of_work, salary, pincode, status):
        self.email = email
        self.photo_urls = json.dumps(photo_urls)
        self.dob = dob
        self.status = status
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.address = address
        self.hash_password = hash_password
        self.aadhar_number = aadhar_number
        self.bank_acc_no = bank_acc_no
        self.gender = gender
        self.available_Days = available_Days
        self.available_Hours = available_Hours
        self.preferred_work = preferred_work
        self.type_of_work = type_of_work
        self.salary = salary
        self.public_id = public_id

    def get_photo_urls(self, photo_urls):   
        return json.loads(photo_urls) if self.photo_urls else []

    def __repr__(self):
        return "<{}:{}>".format(id, self.first_name + " " + self.last_name)
    

@db.event.listens_for(Worker, 'before_insert')
def set_created_at(mapper, connection, target):
    target.created_at = datetime.utcnow()

@db.event.listens_for(Worker, 'before_update')
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()