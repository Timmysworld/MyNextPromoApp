from flask_app import app
from flask_app.controllers import admins, employees


if __name__ == "__main__":
    app.run(debug=True, port = 8000)