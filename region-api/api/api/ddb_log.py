from flask import render_template, Blueprint
from requests import post
from json import dumps

bp = Blueprint('ddb_log', __name__)


@bp.route('/data', methods=['GET'])
def retrieve_list():
    ddb_employees = get_ddb_logs()
    return render_template('Angandatalist.html', awc_data=ddb_employees)

def get_ddb_logs():
    try:
        url = "http://127.0.0.1:5000/get-by-state-id"
        payload = dumps({
            "criteria": "state_id",
            "value": "7"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = post(url, headers=headers, data=payload).json()
        return response.get('data')
    except Exception as e:
        print(e)
        return [{}] 