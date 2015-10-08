from parameters import parameters

# Statement for enabling the development environment
DEBUG = parameters['debug']
print "Config loaded with debug {}".format(DEBUG)

#SERVER_NAME = parameters['servername']

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'mysql://{0:s}:{1:s}@{2:s}:{3:d}/{4:s}'.format(
    parameters['dbuser'],
    parameters['dbpassword'],
    parameters['dbhost'],
    parameters['dbport'],
    parameters['dbname']
)

DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "fxfxqfvqgqcqfqijqfciqjixi354545Icijrmcijfeicj5J3OICJ53Mjcmjrocij"

# Secret key for signing cookies
SECRET_KEY = "EUHFNXLUEHfnxluehflnxuzehf343U483UCN3URNCP3Unczeficjnzeifjc34U39URCN3RUCNfjcnijfcm"

# Flask-Security config
SECURITY_LOGIN_USER_TEMPLATE = 'security/my_login_user.html'
SECURITY_REGISTER_USER_TEMPLATE = 'security/my_register_user.html'
SECURITY_REGISTERABLE = True
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'fncoqzifjcqmzoeifjnvqmghcqnmfiqxeje,zmqcgnixzmnijcgimcqjergiomc,qejiormgcjnq'
SECURITY_UNAUTHORIZED_VIEW = 'security.login'

# Disable blocking of redirections by Flask Debug Toolbar extension
DEBUG_TB_INTERCEPT_REDIRECTS = False
