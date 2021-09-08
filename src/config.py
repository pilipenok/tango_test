import os

app_name = 'tango'

DEBUG = os.environ.get('DEBUG', False)
PROFILE = os.environ.get('PROFILE', False)

predictions_endpoint = 'http://127.0.0.1:5000/prediction'