from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS  # Import Flask-CORS
from config.db import db
from routes.user import user_bp
from models.user import User
from models.student import Student
from models.suclass import SUClass


app = Flask(__name__)

# Configure Flask-CORS with the necessary options
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to your actual secret key


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anant:123@localhost/testdbpython'
db.init_app(app)

app.register_blueprint(user_bp, url_prefix='/api')

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True,port=3032)



