from app.main import db
from datetime import datetime

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    pincode = db.Column(db.String(50))
    address = db.Column(db.String(255))
    created_at =  db.Column(db.DateTime, default=datetime.utcnow,nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=False)
    hash_password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)

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
    
    def __init__(self, email, public_id, phone_number, first_name, last_name, city, state, address,hash_password, role, pincode):
        self.email = email
        self.pincode = pincode
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.address = address
        self.hash_password = hash_password
        self.public_id = public_id
        self.role = role
        

    def __repr__(self):
        return "<{}:{}>".format(id, self.first_name + " " + self.last_name)
    

@db.event.listens_for(User, 'before_insert')
def set_created_at(mapper, connection, target):
    target.created_at = datetime.utcnow()

@db.event.listens_for(User, 'before_update')
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()