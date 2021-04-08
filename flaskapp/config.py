import os
class Config:

    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'

    # < connection Database >
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/twitter'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # SEnd to mail outgoing
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    # app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    # mail = Mail(app)