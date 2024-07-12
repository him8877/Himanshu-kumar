from flask import Blueprint, request
from lib.mongodb import MongoDB
from werkzeug.exceptions import BadRequest


bp = Blueprint('pt_region', __name__)


@bp.route('/get-by-state-id', methods=['POST'])
def get_by_state_id():
    attributes = ('district_id', 'project_id', 'state_id', 'awc_id')
    try:
        data = request.get_json()
    except BadRequest:
        return {'error': f'Criteria and value missing'}, 422
    criteria = data.get('criteria')
    try:
        value = int(data.get('value'))
    except ValueError:
        return {'error': "Value should be the numeric value"}, 422

    if criteria is None or value is None:
        return {'error': f'Criteria and value missing'}, 422
    if criteria not in attributes:
        return {'error': f'Valid Criteria : {attributes}'}, 400

    mongodb_obj = MongoDB(collection_name='region_collection')
    records = mongodb_obj.read_data(attribute=criteria, value=value)
    return {'data': records}, 200
