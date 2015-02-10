from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

payment = Blueprint('payment', __name__,
                        template_folder='templates')

@payment.route('/', methods=['GET', 'POST'])
def index():
    return "payment page!"

@payment.route('/createplan', methods=['GET'])
def create_billing_plan():
    #TODO sets up the billing plans for the application
    return "payment page!"

@payment.route('/initiate/<plan>', methods=['GET'])
def initiate_payment(plan):
    #TODO: Create billing agreement and redirect user to approval
    return "plan id is %s" % plan
    
@payment.route('/execute/<payment_token>', methods=['GET'])
def execute_billing_agreement(plan):
    #TODO: Create billing agreement and exec
    return "plan id is %s" % plan

