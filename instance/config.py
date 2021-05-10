import os 

database_file = "sqlite:///{}".format(os.path.join(os.getcwd(), "ConsignmentDB.db"))

class Config(object):
  """Parent Configuration Class"""
  DEBUG = False
  CSRF_ENABLED = True
  SECRET = os.getenv('SECRET')
  SQLALCHEMY_DATABASE_URI = database_file

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    CORS_ENABLED = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(os.getcwd(), "ConsignmentDB_test.db"))
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(os.getcwd(), "ConsignmentDB_staging.db"))


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}