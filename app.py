from flask import Flask, render_template, request, g, redirect, url_for
from flask_login import LoginManager, UserMixin
import json, sqlite3, flask_login

login_manager = LoginManager()

app = Flask(__name__, static_url_path='')
app.secret_key = 'super secret string'

login_manager.init_app(app)

DATABASE = "database.db"

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    temp = []
    for user in query_db('select * from admin'):
        temp.append(user)
    if email not in temp:
        return

    user = User()
    user.id = email

    temp = query_db('SELECT password FROM admin WHERE username = ?', [email], one=True)
    user.is_authenticated = request.form['password'] == str(temp).split("'")[1]

    return user

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def database():
    global conn, cursor
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/inventory')
@flask_login.login_required
def inventory():
    inv = []
    database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        temp = dict(name=data[1],qty=data[2],price=data[3])
        inv.append(temp)

    return render_template("inv.html",inv=inv)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    email = request.form['email']
    temp = query_db('SELECT password FROM admin WHERE username = ?', [email], one=True)
    print str(temp).split("'")[1]

    if str(temp).split("'")[1] == request.form['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('inventory'))
    msg = "Wrong username/password"
    return render_template("login.html", msg=msg)

@app.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return render_template("index.html")

@app.route("/add", methods=['GET', 'POST'])
@flask_login.login_required
def add_prod():
    if request.method == 'GET':
        return render_template("addProd.html")

    database()
    print request.form["name"]
    cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price) VALUES(?, ?, ?)",(str(request.form['name']), int(request.form['QTY']), int(request.form['price'])))
    conn.commit()
    cursor.close()
    conn.close()
    return render_template("addProd.html", msg="Succees")

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template("login.html")

@app.context_processor
def inject_Cname():
    name = query_db("SELECT company_name FROM config")
    return dict(Cname=str(name).split("'")[1])

