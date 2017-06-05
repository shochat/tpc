import json

from flask import Blueprint, jsonify
from flask import render_template
from flask import request
from model.plan import Plan
from model.user_details import UserDetails, UserDetailsMock

controllers = Blueprint('controllers', __name__, template_folder='templates')


@controllers.route('/')
def form():
    return render_template('index.html')


@controllers.route('/index.html')
def form_from_index():
    return render_template('index.html')


@controllers.route('/test-application')
def test_application():
    return 'Application looks OK'


@controllers.route('/create-plan', methods=['POST', 'GET'])
def create_plan():
    form_details = request.get_json()
    # print(form_details)
    user_details = UserDetails(form_details)
    p = Plan(user_details)
    # mock = UserDetailsMock()
    # p = Plan(mock)
    p.create()
    # plan = p.serialize()
    # print(plan)
    return jsonify(p.serialize())
    # results = p.serialize()
    # return render_template('new-results.html', results=results)
