# sgpnapi

How to run on Gunicorn

✅ 1. wsgi.py

Create this in /var/www/py/sgpnapi/wsgi.py:

from app import app

if __name__ == "__main__":
    app.run()
Make sure your app.py looks like this at the top:
from flask import Flask
app = Flask(__name__)
✅ 2. Gunicorn Systemd Service

Create the service file:

sudo nano /etc/systemd/system/sgpnapi.service
Paste:

[Unit]
Description=Gunicorn instance to serve sgpnapi
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/py/sgpnapi
Environment="PATH=/var/www/py/sgpnapi/venv/bin"
ExecStart=/var/www/py/venv/bin/gunicorn --workers 3 --bind unix:/var/www/py/sgpnapi.sock wsgi:app

[Install]
WantedBy=multi-user.target
Enable the service:

sudo systemctl daemon-reload
sudo systemctl start sgpnapi
sudo systemctl enable sgpnapi
sudo systemctl status sgpnapi
✅ 3. Nginx Site Config

Create Nginx config:

sudo nano /etc/nginx/sites-available/sgpnapi
Paste:

server {
    listen 80;
    server_name sgpnapi.plantnavigator.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/py/sgpnapi.sock;
    }
}
Enable the site:

sudo ln -s /etc/nginx/sites-available/sgpnapi /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
✅ 4. Open Firewall Ports

sudo ufw allow 'Nginx Full'
Also in AWS EC2 > Security Groups, make sure ports 80 and 443 are open.

✅ 5. Install Dependencies

Make sure Gunicorn is installed inside your virtualenv:

cd /var/www/py/sgpnapi
source venv/bin/activate
pip install gunicorn flask
✅ Final Test

Visit:

http://sgpnapi.plantnavigator.com/
Or use Postman to test:

POST http://sgpnapi.plantnavigator.com/add_user






 For windows:

 project folder path in Windows(C):   C:\xampps\htdocs\sgpnapi
 
 step 1: database configuaration :
 
 class Config:
    TEMPLATE_FOLDER = 'app/templates'
    STATIC_FOLDER = 'app/static'
	# MySQL Database Configuration
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'plantnavigator_production'
    MYSQL_PORT = 3306
    #email configuration
    SECRET_KEY = 'HTS_S@@rgummi@2025'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'abcd@iqhired.com'    (Replace your mail username here)
    MAIL_PASSWORD = 'abcdiqHired@123'       (Replace your mail password here)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/plantnavigator_production'
 
 step 2: Run for this command :   -m pip install flask
 
 C:/Users/IQH-Dev01/AppData/Local/Programs/Python/Python313/python.exe -m pip install flask
 
 
step 3:  pip install flask flask_sqlalchemy flask_jwt_extended mysql-connector-python   (if step 3 is not working, try it step 4)

step 4: Run the following command in your terminal:

pip install flask flask_sqlalchemy flask_jwt_extended pymysql


note : 

This will install:

flask – core web framework

flask_sqlalchemy – database ORM

flask_jwt_extended – for login/auth

pymysql – required for MySQL connection with SQLAlchemy



step 5: If you're using Python 3.13 or any other version, make sure you're using the correct pip:

C:/Users/IQH-Dev01/AppData/Local/Programs/Python/Python313/python.exe -m pip install flask flask_sqlalchemy flask_jwt_extended pymysql


step 6: After Installing
Try running your app again in your terminal:

python wsgi.py


step 7: Run your application in your Browser

http://127.0.0.1:5000/

step 8: GET(method) api url for your local & postman, you can use this Url (API url may change according to the Your requirement), This is for your Reference

http://127.0.0.1:5000/station_events?event_type_id=5&line_id=3&start_time=2024-05-13%2007:39&end_time=2025-05-14%2007:39








