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


@mod_home.route('/search/user/<username>')
def searchuser(username):
    user = User.all().filter(User.name.like('%' + username + '%'))
    return jsonify(search_result=[i.serialize for i in user])


@mod_home.route('/add/user/<username>')
def adduser(username):
    user = User.create(name=username, description="hehehe")
    return str(user.id)


@mod_home.route('/delete/user/<user_id>')
def delete(user_id):
    user = User.get(user_id)
    if user:
        user.delete()
        return "delete success"
    else:
        return "delete fail"
