
from flask_restful import reqparse,abort,Api,Resource,output_json
from API.models import db,Patient,Drug_info,Work_log,server
import json
import datetime
from API.schema import patients_schema

api= Api(server)

workstatus=[1,2,3,4]
def abort_if_workstatus_dosenot_exist(status_id):
    if status_id not in workstatus:
        abort(404,message="The status {} dosen't exist".format(status_id))

def abort_if_patient_dosenot_exist(status_id):
    abort(404,message="No patient as the status {} ".format(status_id))

parser=reqparse.RequestParser()
parser.add_argument('state',type=int)
parser.add_argument('id',type=int)

class PatientInfo(Resource):
    def get(self,state):
        abort_if_workstatus_dosenot_exist(state)
        patients = Patient.query.filter_by(state=state).all()
        if len(patients)!=0:
            return patients_schema.dump(patients)
        else:
            abort_if_patient_dosenot_exist(state)

class PatientDrugInfo(Resource):
    def get(self,patient_id):
        drugs = Drug_info.query.filter_by(patient_id=patient_id).all()
        if len(drugs)!=0:
            return patients_schema.dump(drugs)

class UpdatePatientState(Resource):
    def post(self):
        args=parser.parse_args()
        abort_if_workstatus_dosenot_exist(args.get('state'))
        patient = Patient.query.get(args.get('id'))
        patient.state=args.get('state')
        db.session.commit()
        return 201

class UpdatePatientDrugState(Resource):
    def post(self,state):
        args=parser.parse_args()
        abort_if_workstatus_dosenot_exist(args.get('state'))
        patient = Patient.query.get(args.get('id'))
        patient.state=args.get('state')
        db.session.commit()
        return 201

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)

api.add_resource(PatientInfo,'/patient/<int:state>')
api.add_resource(UpdatePatientState,'/patient/updatestate')

if __name__ == '__main__':
    server.run(debug=True)