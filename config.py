import os
from parameters import parameters

DEBUG = parameters['debug']
print("Config loaded with debug {}".format(DEBUG))

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = '{:s}://{:s}:{:s}@{:s}:{:d}/{:s}'.format(
    parameters['db_pdo'],
    parameters['db_user'],
    parameters['db_password'],
    parameters['db_host'],
    parameters['db_port'],
    parameters['db_name'])
SQLALCHEMY_TRACK_MODIFICATIONS = True

THREADS_PER_PAGE = 2
CSRF_ENABLED = True
CSRF_SESSION_KEY = "fxfxqfvqgqcqfqijqfciqjixi354545Icijrmcijfeicj5J3OICJ53Mjcmjrocij"
SECRET_KEY = "EUHFNXLUEHfnxluehflnxuzehf343U483UCN3URNCP3Unczeficjnzeifjc34U39URCN3RUCNfjcnijfcm"

# Flask-Security config
SECURITY_LOGIN_USER_TEMPLATE = 'firewall/login.html'
SECURITY_REGISTER_USER_TEMPLATE = 'firewall/register.html'
SECURITY_CHANGE_PASSWORD_USER_TEMPLATE = 'firewall/change.html'
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'fncoqzifjcqmzoeifjnvqmghcqnmfiqxeje,zmqcgnixzmnijcgimcqjergiomc,qejiormgcjnq'
SECURITY_UNAUTHORIZED_VIEW = 'security.login'
SECURITY_SEND_REGISTER_EMAIL = False

DEBUG_TB_INTERCEPT_REDIRECTS = False
