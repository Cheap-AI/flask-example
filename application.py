from secrets_ import SOURCE,MEANINGOFLIFE
import secrets
from flask import Flask


# print(f" {SOURCE}and seriously {MEANINGOFLIFE}")
# print(secrets.randbits(7))
application = Flask(__name__)
app = application


@app.route('/')
def hello_world():
    return f'You say I say {SOURCE} and {MEANINGOFLIFE}'
