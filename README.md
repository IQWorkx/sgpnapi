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