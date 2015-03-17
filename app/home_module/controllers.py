# Import flask dependencies
from flask import Blueprint, jsonify
from flask import request
from app import db
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
    user = User.query.paginate(page=int(page), error_out=False).items
    return jsonify(users=[i.serialize for i in user])


@mod_home.route('/search/user/<username>')
def searchuser(username):
    user = User.query.filter(User.name.like('%' + username + '%'))
    return jsonify(search_result=[i.serialize for i in user])


@mod_home.route('/add/user/<username>')
def adduser(username):
    user = User(username)
    db.session.add(user)
    db.session.commit()
    return str(user.id)
