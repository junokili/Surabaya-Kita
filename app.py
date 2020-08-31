import os
from flask import (Flask, render_template, redirect,
                   flash, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/get_events')
def get_events():
    events = mongo.db.events.find()
    return render_template("events.html", events=events)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check for existing user
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        if existing_user:
            # match password
            if check_password_hash(
               existing_user['password'], request.form.get('password')):
                session['user'] = request.form.get('username').lower()
                flash("Welcome, {}".format(request.form.get('username')))
                return redirect(url_for('my_profile',
                                username=session['user']))
            else:
                # invalid password
                flash("Incorrect username and / or password")
                return redirect(url_for('login'))
        else:
            # user doesn't exist
            flash("Incorrect username and / or password")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # check if user already exists
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for('sign_up'))

        sign_up = {
            'username': request.form.get('username').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(sign_up)

        # add new user into session
        session['user'] = request.form.get('username').lower()
        flash("Registration succesful")
        return redirect(url_for('my_profile', username=session['user']))
    return render_template('sign_up.html')


@app.route('/my_profile/<username>', methods=["GET", "POST"])
def my_profile(username):
    # get session username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session['user']:
        return render_template('my_profile.html', username=username)

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    flash("You have been logged out")
    session.pop('user')
    return redirect(url_for('login'))


@app.route('/get_categories')
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template('categories.html', categories=categories)


@app.route('/add_category', methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            'category_name': request.form.get('category_name')
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added!")
        return redirect(url_for('get_categories'))

    return render_template('add_category.html')


@app.route('/edit_category/<category_id>', methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            'category_name': request.form.get('category_name')
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category updated!")
        return redirect(url_for('get_categories'))
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template('edit_category.html', category=category)


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    flash("Category deleted")
    return redirect(url_for('get_categories'))


@app.route('/create_event', methods=["GET", "POST"])
def create_event():
    if request.method == "POST":
        free_event = "on" if request.form.get("free_event") else "off"
        event = {
            "category_name": request.form.get("category_name"),
            "event_name": request.form.get("event_name"),
            "event_description": request.form.get("event_description"),
            "free_event": free_event,
            "event_date": request.form.get("event_date"),
            "created_by": session["user"],
        }
        mongo.db.events.insert_one(event)
        flash("New event created!")
        return redirect(url_for('get_events'))

    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template('create_event.html', categories=categories)


@app.route('/edit_event/<event_id>', methods=["GET", "POST"])
def edit_event(event_id):
    if request.method == "POST":
        free_event = "on" if request.form.get("free_event") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "event_name": request.form.get("event_name"),
            "event_description": request.form.get("event_description"),
            "free_event": free_event,
            "event_date": request.form.get("event_date"),
            "created_by": session["user"],
        }
        mongo.db.events.update({"_id": ObjectId(event_id)}, submit)
        flash("Event updated!")

    event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template('edit_event.html',
                           event=event, categories=categories)


@app.route('/delete_event/<event_id>')
def delete_event(event_id):
    mongo.db.events.remove({"_id": ObjectId(event_id)})
    flash("Event deleted")
    return redirect(url_for('get_events'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
