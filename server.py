from main import app

#  flask is not suitable for production, so let's use gunicorn
if __name__ == "__main__":
    app.run()
