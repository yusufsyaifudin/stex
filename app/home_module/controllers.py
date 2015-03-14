# Import flask dependencies
from flask import Blueprint, jsonify
from app.home_module.models.user import User

# Define the blueprint: 'home', set its url prefix: app.url/
mod_home = Blueprint('home', __name__)
# mod_home = Blueprint('home', __name__, url_prefix='/')


@mod_home.route("/", methods=["GET"])
def hello():
    user = User.query.all()
    return jsonify(users=[i.serialize for i in user])


@mod_home.route('/search/user/<username>')
def searchuser(username):
    user = User.query.filter(User.name.like('%' + username + '%'))
    return jsonify(search_result=[i.serialize for i in user])


@mod_home.route('/add/user')
def adduser():
    return 'insert'
