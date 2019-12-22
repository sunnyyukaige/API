from flask_sqlalchemy import SQLAlchemy
from flask import Flask

server=Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Kaige@8531917@localhost:3306/test?charset=utf8'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(server)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(100), nullable=True)
    mzh = db.Column(db.VARCHAR(100), nullable=True)
    seat_no = db.Column(db.VARCHAR(10), nullable=True)
    patient_type = db.Column(db.VARCHAR(10), nullable=True)
    state = db.Column(db.INTEGER, nullable=True)
    date_time = db.Column(db.DATETIME, nullable=True)

    __tablename__ = 't_patient'

    def __init__(self, id, name,mzh,seat_no,patient_type,state,date_time):
        self.id = id
        self.name = name
        self.mzh = mzh
        self.seat_no = seat_no
        self.patient_type = patient_type
        self.date_time = date_time


class Drug_info(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, nullable=True)
    group_no = db.Column(db.INTEGER, nullable=True)
    cf_no = db.Column(db.VARCHAR(100), nullable=True)
    drug_name = db.Column(db.VARCHAR(100), nullable=True)
    dose = db.Column(db.VARCHAR(100), nullable=True)
    unit = db.Column(db.VARCHAR(100), nullable=True)
    patient_state = db.Column(db.INTEGER, nullable=True)
    state = db.Column(db.INTEGER, nullable=True)

    __tablename__ = 't_drug_info'



class Work_log(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    operation_type = db.Column(db.VARCHAR(50), nullable=True)
    operation_name = db.Column(db.VARCHAR(50), nullable=True)
    operation_no = db.Column(db.VARCHAR(100), nullable=True)
    patient_id = db.Column(db.Integer, nullable=True)
    remarks = db.Column(db.VARCHAR(255), nullable=True)
    date_time = db.Column(db.DATETIME, nullable=True)

    __tablename__ = 't_work_log'

