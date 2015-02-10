from flask import Flask
import os
app = Flask(__name__)

from blueprints.config import blueprint_config
for config in blueprint_config:
    app.register_blueprint(config['class'], url_prefix=config['prefix'])

if 'ENV' in os.environ and os.environ['ENV'] == 'debug':
    app.config['DEBUG'] = True
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)