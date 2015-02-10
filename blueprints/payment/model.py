from firebase import firebase
import datetime

connection = firebase.FirebaseApplication('https://smu-paypal-demo.firebaseio.com', None)
plan_model = '/plans'
agreement_model = '/agreement'

return_url = "http://ulkkbc1e933e.laurenceputra.koding.io:3000/payment/execute/"
cancel_url = "http://ulkkbc1e933e.laurenceputra.koding.io:3000/payment/cancel/"
payment_plans = {
    "2999": {
        "description": "Regular Plan",
        "merchant_preferences": {
            "auto_bill_amount": "yes",
            "cancel_url": cancel_url,
            "initial_fail_amount_action": "continue",
            "max_fail_attempts": "1",
            "return_url": return_url,
            "setup_fee": {
                "currency": "SGD",
                "value": "0"
            }
        },
        "name": "Regular Plan",
        "payment_definitions": [
            {
                "amount": {
                    "currency": "SGD",
                    "value": "29.99"
                },
                "cycles": "0",
                "frequency": "MONTH",
                "frequency_interval": "1",
                "name": "Regular 1",
                "type": "REGULAR"
            },
            {
                "amount": {
                    "currency": "SGD",
                    "value": "19.99"
                },
                "cycles": "1",
                "frequency": "MONTH",
                "frequency_interval": "1",
                "name": "Trial 1",
                "type": "TRIAL"
            }
        ],
        "type": "INFINITE"
    },
    '5999': {
        "description": "Premium Plan",
        "merchant_preferences": {
            "auto_bill_amount": "yes",
            "cancel_url": cancel_url,
            "initial_fail_amount_action": "continue",
            "max_fail_attempts": "1",
            "return_url": return_url,
            "setup_fee": {
                "currency": "SGD",
                "value": "0"
            }
        },
        "name": "Premium Plan",
        "payment_definitions": [
            {
                "amount": {
                    "currency": "SGD",
                    "value": "59.99"
                },
                "cycles": "0",
                "frequency": "MONTH",
                "frequency_interval": "1",
                "name": "Premium 1",
                "type": "REGULAR"
            },
            {
                "amount": {
                    "currency": "SGD",
                    "value": "39.99"
                },
                "cycles": "1",
                "frequency": "MONTH",
                "frequency_interval": "1",
                "name": "Trial 2",
                "type": "TRIAL"
            }
        ],
        "type": "INFINITE"
    }

}

def create_agreement_data(tier, plan_id, address):
    return {
        "name": "Regular Plan" if tier == '2999' else "Premium Plan",
        "description": "Regular Plan" if tier == '2999' else "Premium Plan",
        "start_date": (datetime.datetime.now() + datetime.timedelta(days = 5)).isoformat()[0:19] + 'Z',
        "plan":{
            "id": plan_id
        },
        "payer": {
            "payment_method": "paypal"
        },
        "shipping_address": {
            "line1": address["line1"] if "line1" in address else "",
            "line2": address["line2"] if "line2" in address else "",
            "city": address["city"] if "city" in address else "",
            "state": address["state"] if "state" in address else "",
            "postal_code": address["postal_code"] if "postal_code" in address else "",
            "country_code": address["country_code"] if "country_code" in address else ""
        }
    }
