from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate API</h> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')

def api(in_cur, out_cur):


app.run(host='')