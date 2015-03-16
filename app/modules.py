from flask import render_template
from app import app

# Import a module / component using its blueprint handler variable
from app.home_module.controllers import mod_home


# Register blueprint(s)
# app.register_blueprint(xyz_module)
# ..
app.register_blueprint(mod_home)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
