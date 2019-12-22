from flask_marshmallow import Marshmallow
from API.models import server
ma=Marshmallow(server)
class PatientSchema(ma.Schema):
    class Meta:
        fields = ('date_time','id','name'
            ,'mzh','seat_no',
            'patient_type','state')

class PatientDrugSchema(ma.Schema):
    class Meta:
        fields = ('id', 'patient_id', 'group_no'
            , 'cf_no', 'drug_name',
            'dose','unit','patient_state','state')

class PatientLogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'operation_type', 'operation_name'
            , 'operation_no', 'patient_id',
            'remarks','date_time')
patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
patient_drug_schema = PatientDrugSchema()
patients_drug_schema = PatientDrugSchema(many=True)
patient_log_schema = PatientLogSchema()
patients_log_schema = PatientLogSchema(many=True)

