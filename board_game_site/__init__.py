from flask import Flask, request
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from flask_migrate import Migrate
from board_game_site.models import db as root_db, login_manager, ma


from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

root_db.init_app(app)
migrate = Migrate(app, root_db)

login_manager.init_app(app)


# Specifying a route for non authorized users
login_manager.login_view = 'auth.signin'

ma.init_app(app)
CORS(app)
from board_game_site import models