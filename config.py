# coding: utf8

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
# Login
SECURITY_LOGIN_USER_TEMPLATE = 'firewall/login.html'
SECURITY_CONFIRMABLE = False
SECURITY_MSG_INVALID_PASSWORD = (u"Mauvais mot de passse", 'error')

# Register
SECURITY_REGISTERABLE = True
SECURITY_REGISTER_USER_TEMPLATE = 'firewall/register.html'
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_MSG_PASSWORD_INVALID_LENGTH = (u"Veuillez choisir un mot de passe d'au moins 6 caractères", 'error')
SECURITY_MSG_USER_DOES_NOT_EXIST = (u"Aucun utilisateur avec cet e-mail n'a été trouvé !", 'error')

# Change password
SECURITY_CHANGEABLE = True
SECURITY_CHANGE_PASSWORD_TEMPLATE = 'firewall/change.html'
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
SECURITY_MSG_PASSWORD_CHANGE = (u'Votre mot de passe a bien été changé !', 'success')

# Other
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'fncoqzifjcqmzoeifjnvqmghcqnmfiqxeje,zmqcgnixzmnijcgimcqjergiomc,qejiormgcjnq'
SECURITY_UNAUTHORIZED_VIEW = 'security.login'

# Flask-DebugToolbar
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Sentry
SENTRY_DSN = 'https://0c0bacc3890a47939c6e3b37056255eb:4d378307a6624eec8d1f0c68cd3c995a@sentry.io/95589'
