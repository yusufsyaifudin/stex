# Import flask dependencies
from flask import Blueprint, jsonify
from flask import request
from app.home_module.models.user import User

# Define the blueprint: 'home', set its url prefix: app.url/
mod_home = Blueprint('home', __name__)
# mod_home = Blueprint('home', __name__, url_prefix='/')


@mod_home.route("/", methods=["GET"])
def hello():
    try:
        page = request.args.get('page')
        if page is None:
            page = 1
    except Exception:
        page = 1
    user = User.all().paginate(page=int(page))
    return jsonify(users=[i.serialize for i in user])


@mod_home.route('/search/user/<email>')
def searchuser(email):
    user = User.all().filter(User.email.like('%' + email + '%'))
    return jsonify(search_result=[i.serialize for i in user])


@mod_home.route('/add/user/<username>/<email>/<password>')
def adduser(username, email, password):
    try:
        user = User.create(
            name=username,
            email=email,
            password=password
        )
        return str(user.id)
    except Exception as e:
        return str(e)


@mod_home.route('/delete/user/<user_id>')
def delete(user_id):
    user = User.get(user_id)
    if user:
        user.delete()
        return "delete success"
    else:
        return "delete fail"
