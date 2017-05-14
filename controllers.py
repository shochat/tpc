import json
from flask import Blueprint
from flask import request
from model.plan import Plan
from model.user_details import UserDetails

controllers = Blueprint('controllers', __name__, template_folder='templates')


@controllers.route('/create-plan', methods=['POST', 'GET'])
def create_plan():
    user_details = UserDetails(request.form)
    p = Plan(user_details)
    p.create()
    return json.dumps(p.serialize())
