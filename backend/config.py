class Config():
    DEBUG = False #disables debug mode by default
    SQLALCHEMY_TRACK_MODIFICATIONS = False #disables track modifications to save memory in SQLAlchemy
    
class LocalDevelopmentConfig(Config):
    DEBUG = True #enables debug mode for local development
    SQLALCHEMY_DATABASE_URI= 'sqlite:///local.db.sqlite3' #URI for SQLite database
    SECURITY_PASSWORD_HASH = 'bcrypt'#Specifies the hashing algorithm for password's security
    SECURITY_PASSWORD_SALT = 'this-is-a-salt' #Salt used to make hashing passwords more secure
    SECRET_KEY="super_secret_key" #Secret key for signing cookies and other cryptographic operations (security purposes)
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token' #custom header for token authentication
    WTF_CSRF_ENABLED = False #Disables CSRF protection for forms (not recommended for production / since using JavaScript frontend)
    