from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
# Gunicorn command to run the app
# gunicorn --bind