import datetime
from flask import Blueprint
from flask import render_template
from flask import request

from model.plan import Plan, RaceDistance
from model.user_details import UserDetails

controllers = Blueprint('controllers', __name__, template_folder='templates')


@controllers.route('/')
def form():
    return render_template('index.html')


@controllers.route('/create-plan', methods=['POST', 'GET'])
def create_plan():
    user_details = UserDetails(request.form)
    p = Plan(user_details)
    p.create()
    return render_template('results.html', results=p.weekly_plan_list)
