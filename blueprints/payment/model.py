from firebase import firebase

connection = firebase.FirebaseApplication('https://smu-paypal-demo.firebaseio.com', None)
plan_model = '/plans'
agreement_model = '/agreement'

return_url = "http://ulkkbc1e933e.laurenceputra.koding.io:3000/payment/execute/"
cancel_url = "http://ulkkbc1e933e.laurenceputra.koding.io:3000/payment/cancel/"
payment_plans = {
    '2999': {
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