class Config(object):
    SECRET_KEY = "xrdtfvbyuhnjimuygtfrdessdfnhhmjjygh65hrytrytr"
    debug = True


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "tutti.conductor@gmail.com"
    SQLALCHEMY_DATABASE_URI = "mysql+gaerdbms:///tuttidb?instance=tutti-alpha-seulki:tuttinstance"
    migration_directory = "migrations"
