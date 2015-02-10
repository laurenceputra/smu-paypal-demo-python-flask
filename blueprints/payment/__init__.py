from flask import Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound
import paypalrestsdk
import model

payment = Blueprint('payment', __name__,
                        template_folder='templates')

@payment.route('/', methods=['GET', 'POST'])
def index():
    return "payment page!"

@payment.route('/createplan', methods=['GET'])
def create_billing_plan():
    plan_ids = []
    for plan in model.payment_plans:
        #creating a plan for each plan in the model
        billing_plan = paypalrestsdk.BillingPlan(model.payment_plans[plan])
        if billing_plan.create() and billing_plan.activate():
            billing_plan = paypalrestsdk.BillingPlan.find(billing_plan.id)
            if billing_plan.state == 'ACTIVE':
                #Save Plan to Firebase
                model.connection.put(model.plan_model, plan.replace('.',''), {'id': billing_plan.id})
                plan_ids.append(billing_plan.id)
            else:
                raise Exception("billing_plan not activated")
        else:
            raise Exception("billing_plan not created")
    return jsonify({
        'status':'success',
        'data': plan_ids
    })

@payment.route('/initiate/<plan>', methods=['GET'])
def initiate_payment(plan):
    #TODO: Create billing agreement and redirect user to approval
    return "plan id is %s" % plan
    
@payment.route('/execute/<payment_token>', methods=['GET'])
def execute_billing_agreement(plan):
    #TODO: Create billing agreement and exec
    return "plan id is %s" % plan

