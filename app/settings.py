class Config(object):
    # give your own values to 2 variables below
    FACEBOOK_APP_ID = "944323692250762"
    FACEBOOK_APP_SECRET = "207996ac76593a7fe2dd9930ecb79ce5"
    SECRET_KEY = "xrdtfvbyuhnjimuygtfrdessdfnhhmjjygh65hrytrytr"
    debug = True


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "tutti.conductor@gmail.com"
    SQLALCHEMY_DATABASE_URI = "mysql+gaerdbms:///tuttidb?instance=tutti-alpha-seulki:tuttinstance"
    migration_directory = "migrations"
    
