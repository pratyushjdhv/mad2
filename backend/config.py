class config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class local(config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite3"
    DEBUG = True
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = "wowsecrettobypassattack"
    SECRET_KEY = "veryverysecretkey"

    WTF_CSRF_ENABLED = False
