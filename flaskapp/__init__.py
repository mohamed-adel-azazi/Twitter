from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskapp.config import Config
#######################################
# to send an email:
from flask_mail import Mail
import os
import smtplib
#################################



#################################################################################

# initilization database and pass my app
db = SQLAlchemy()
# initilization hash-password
bcrypt = Bcrypt()
# initilization LoginManager
login_manager = LoginManager()
# You must be logged in to see account page
login_manager.login_view = 'users.login'
# flash style message of (login_manager.login_view)
login_manager.login_message_category = 'info'
###########################################################

mail = Mail()

#########################################################




def create_app(config_class=Config):
    # initilization  My app
    app = Flask(__name__)
    app.config.from_object(Config)

     # initilization database and pass my app
    db.init_app(app)
    # initilization hash-password
    bcrypt.init_app(app)
    # initilization LoginManager
    login_manager.init_app(app)
    # initilization mail
    mail.init_app(app)



    from flaskapp.users.routes import users # Blueprint
    from flaskapp.posts.routes import posts # Blueprint
    from flaskapp.main.routes import main # Blueprint
    from flaskapp.errors.handlers import errors # Blueprint

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
