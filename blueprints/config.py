from payment import payment

blueprint_config = [
    {
        'class': payment,
        'prefix': '/payment'
    }
]