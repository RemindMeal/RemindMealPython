from parameters import parameters

# Statement for enabling the development environment
DEBUG = parameters['debug']
print "Config loaded with debug {}".format(DEBUG)

SERVER_NAME = parameters['servername']

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

# Flask-User config
USER_CHANGE_PASSWORD_URL      = '/user/change-password'
USER_CHANGE_USERNAME_URL      = '/user/change-username'
USER_CONFIRM_EMAIL_URL        = '/user/confirm-email/<token>'
USER_EMAIL_ACTION_URL         = '/user/email/<id>/<action>'     # v0.5.1 and up
USER_FORGOT_PASSWORD_URL      = '/user/forgot-password'
USER_LOGIN_URL                = '/user/login'
USER_LOGOUT_URL               = '/user/logout'
USER_MANAGE_EMAILS_URL        = '/user/manage-emails'
USER_REGISTER_URL             = '/user/register'
USER_RESEND_CONFIRM_EMAIL_URL = '/user/resend-confirm-email'    # v0.5.0 and up
USER_RESET_PASSWORD_URL       = '/user/reset-password/<token>'
