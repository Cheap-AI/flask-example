from secrets_ import SOURCE,MEANINGOFLIFE

from flask import Flask


print(f" {SOURCE}and seriously {MEANINGOFLIFE}")

application = Flask(__name__)
app = application


@app.route('/')
def hello_world():
    return f'You say I say {SOURCE}'
