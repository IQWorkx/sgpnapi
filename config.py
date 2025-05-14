class Config:
    TEMPLATE_FOLDER = 'app/templates'
    STATIC_FOLDER = 'app/static'
	# MySQL Database Configuration
    MYSQL_HOST = '3.219.173.225'
    MYSQL_USER = 'pn_admin_Usr'
    MYSQL_PASSWORD = 'HtsPool2024'
    MYSQL_PN_DB = 'plantnavigator'
    MYSQL_PORT = 3306
    #email configuration
    SECRET_KEY = 'HTS_S@@rgummi@2025'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@gmail.com'
    MAIL_PASSWORD = 'your_password_or_app_password'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://pn_admin_Usr:HtsPool2024@3.219.173.225/plantnavigator'