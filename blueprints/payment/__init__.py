from flask import Blueprint, render_template, abort, jsonify, redirect, request
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
    plans = model.connection.get(model.plan_model, None)
    if plan in plans:
        address = {
            "line1": "1 Temasek Avenue",
            "line2": "#14-01",
            "city": "Singapore",
            "state": "SG",
            "postal_code": "039192",
            "country_code": "SG"
        }
        plan_id = plans[plan]["id"]
        agreement_data = model.create_agreement_data(plan, plan_id, address)
        billing_agreement = paypalrestsdk.BillingAgreement(agreement_data)
        if billing_agreement.create():
            for link in billing_agreement.links:
                if link['rel'] == "approval_url":
                    return redirect(link["href"])
        raise Exception("Creating agreement failed")
    else:
        raise Exception("Invalid Plan")
    return jsonify({
        'status':'failure'
    })
    
@payment.route('/execute/', methods=['GET'])
def execute_billing_agreement():
    if 'token' in request.args:
        token = request.args['token']
        billing_agreement_response = paypalrestsdk.BillingAgreement.execute(token)
        if billing_agreement_response.id:
            return jsonify({
                'status':'success',
                'data': {
                    'id': billing_agreement_response.id
                }
            })
        else:
            raise Exception("Execute failed")
    else:
        raise Exception("Token not found")
    return ({
        'status':'failure'
    })
