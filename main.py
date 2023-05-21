from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

from app.registry.container import Container
from app.interface.views import link_view
from config.setting import SECRET_KEY

csrf = CSRFProtect()

def create_app() -> Flask:
    container = Container()

    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    csrf.init_app(app)

    app.container = container
    app.add_url_rule("/<slug>", "/<slug>", link_view.get_link_by_slug_view)
    app.add_url_rule("/", "/", link_view.create_link_view, methods=['GET', 'POST'])

    bootstrap = Bootstrap()
    bootstrap.init_app(app)

    return app