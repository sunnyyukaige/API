from flask_marshmallow import Marshmallow
from API.models import server
ma=Marshmallow(server)
class PatientSchema(ma.Schema):
    class Meta:
        fields = ('datetime','id','name'
            ,'mzh','seat_no',
            'patient_type')

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)

