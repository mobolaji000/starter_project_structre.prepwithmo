import os
from app.aws import AWSInstance

basedir = os.path.abspath(os.path.dirname(__file__))
awsInstance = AWSInstance()


class Config(object):
    try:
        if os.environ['DEPLOY_REGION'] == 'local':

            os.environ["url_to_start_reminder"] = "http://127.0.0.1:5003/"
            flask_secret_key = os.environ.get('flask_secret_key')
            SECRET_KEY = os.environ.get('flask_secret_key')
            dbUserName = os.environ.get('dbUserNameLocal')
            dbPassword = os.environ.get('dbPasswordLocal')
            SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://' + str(dbUserName) + ':' + str(dbPassword) + '@host/mobolajioo'
            SQLALCHEMY_TRACK_MODIFICATIONS = False

        elif os.environ['DEPLOY_REGION'] == 'dev':

            os.environ["url_to_start_reminder"] = "https://dev-pay-perfectscoremo-7stpz.ondigitalocean.app/"
            flask_secret_key = awsInstance.get_secret("vensti_admin", "flask_secret_key")
            SECRET_KEY = awsInstance.get_secret("vensti_admin", "flask_secret_key")
            dbUserName = awsInstance.get_secret("do_db_cred", "dev_username")
            dbPassword = awsInstance.get_secret("do_db_cred", "dev_password")
            SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://' + str(dbUserName) + ':' + str(dbPassword) + '@app-27fee962-3fa3-41cb-aecc-35d29dbd568e-do-user-9096158-0.b.db.ondigitalocean.com:25060/db'
            SQLALCHEMY_TRACK_MODIFICATIONS = False


        elif os.environ['DEPLOY_REGION'] == 'prod':

            os.environ["url_to_start_reminder"] = "https://pay.perfectscoremo.com/"
            flask_secret_key = awsInstance.get_secret("vensti_admin", "flask_secret_key")
            SECRET_KEY = awsInstance.get_secret("vensti_admin", "flask_secret_key")
            dbUserName = awsInstance.get_secret("do_db_cred", "username")
            dbPassword = awsInstance.get_secret("do_db_cred", "password")
            SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://' + str(dbUserName) + ':' + str(dbPassword) + '@app-36443af6-ab5a-4b47-a64e-564101e951d6-do-user-9096158-0.b.db.ondigitalocean.com:25060/db'
            SQLALCHEMY_TRACK_MODIFICATIONS = False


    except Exception as e:
        print("error in initialization")
        print(e)
        # trigger10

