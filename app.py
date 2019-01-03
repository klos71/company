from flask import Flask, render_template, request
import json

app = Flask(__name__, static_url_path='')
app.secret_key = 'super secret string'

with open('config.json') as f:
    data = json.load(f)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/inventory')
def inventory():
    return render_template("inv.html")


@app.context_processor
def inject_Cname():
    return dict(Cname=data["config"][0]["CompanyName"])
