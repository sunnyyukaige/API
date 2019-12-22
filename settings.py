
class Config:
    DB_URI = 'mysql+pymysql://root:password@host:port/database'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACH_MODIFICATIONS = False