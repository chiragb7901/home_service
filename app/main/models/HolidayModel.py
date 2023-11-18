from app.main import db
from datetime import datetime

class Holiday(db.Model):

    __tablename__ = 'holiday'

    id = db.Column(db.Integer, primary_key=True)
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))
    status = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=False)
    created_at =  db.Column(db.DateTime, default=datetime.utcnow,nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=False)

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
    
    def __init__(self, date ,worker_id, status):
        self.worker_id = worker_id
        self.status = status
        self.date = date

    def __repr__(self):
        return "<{}:{}>".format(id, self.first_name + " " + self.last_name)
    

@db.event.listens_for(Holiday, 'before_insert')
def set_created_at(mapper, connection, target):
    target.created_at = datetime.utcnow()

@db.event.listens_for(Holiday, 'before_update')
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()