from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/hobbyist"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers.member_controller import members_blueprint
from controllers.lesson_controller import lessons_blueprint
from controllers.booking_controller import bookings_blueprint

app.register_blueprint(bookings_blueprint)
app.register_blueprint(lessons_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

from db.seeds import seed
app.cli.add_command(seed)