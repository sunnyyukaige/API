
from flask_restful import reqparse,abort,Api,Resource,output_json
from API.models import db,Patient,Drug_info,Work_log,server
import json
from API.schema import patients_schema,patients_drug_schema,patients_log_schema
from datetime import datetime

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
parser.add_argument('drug_state',type=int)
parser.add_argument('patient_id',type=int)
parser.add_argument('group_no',type=int)
parser.add_argument('operation_type',type=str)
parser.add_argument('operation_name',type=str)
parser.add_argument('operation_no',type=str)
parser.add_argument('patient_id',type=str)



class PatientInfo(Resource):
    def get(self,state):
        abort_if_workstatus_dosenot_exist(state)
        patients = Patient.query.filter_by(state=state).all()
        if len(patients)!=0:
            return patients_schema.dump(patients)
        else:
            abort_if_patient_dosenot_exist(state)



class UpdatePatientState(Resource):
    def post(self):
        args=parser.parse_args()
        abort_if_workstatus_dosenot_exist(args.get('state'))
        patient = Patient.query.filter_by(id=args.get('id'))
        patient.state=args.get('state')
        drugs = Drug_info.query.filter_by(patient_id=args.get('id'))
        drugs.state = 0
        db.session.commit()
        return 201


class PatientDrugInfo(Resource):
    def get(self,patient_id):
        drugs = Drug_info.query.filter_by(patient_id=patient_id).all()
        if len(drugs)!=0:
            return patients_drug_schema.dump(drugs)

class UpdatePatientDrugState(Resource):
    def post(self):
        args=parser.parse_args()
        drugs = Drug_info.query.filter_by(patient_id=args.get('patient_id',group_no=args.get('group_no')))
        drugs.state=args.get('drug_state')
        db.session.commit()
        return 201

class UpdatePatientLog(Resource):
    def post(self):
        args=parser.parse_args()
        logs=Work_log(args.get('operation_type'),args.get('operation_name')
                 ,args.get('patient_id'),args.get('operation_no'),args.get('remarks'),date_time=datetime.now())
        db.session.add(logs)
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
api.add_resource(PatientDrugInfo,'/patient/drug/<int:patient_id>')
api.add_resource(UpdatePatientDrugState,'/patient/drug/updatestate')
api.add_resource(UpdatePatientLog,'/patient/log')

if __name__ == '__main__':
    server.run(debug=True)