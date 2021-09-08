import flask
import config
from app.api import api


app = flask.Flask(__name__, static_url_path="")
#app.register_blueprint(api, url_prefix='/api/v1')
app.register_blueprint(api, url_prefix='')


# TODO: if needed
# from flask_cors import CORS
# CORS(app, resources={r"/api/*": {"origins": ["https://tango.ai", "https://dev.tango.ai"]}})


if config.PROFILE:
    import googlecloudprofiler
    googlecloudprofiler.start(verbose=3, service=config.app_name.lower())
                              #service_account_json_file=config.stackdriver_sa_key_filename)

if config.DEBUG:
    import googleclouddebugger
    googleclouddebugger.enable()
