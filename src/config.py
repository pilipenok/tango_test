import os

app_name = 'tango'

DEBUG = os.environ.get('DEBUG', False)
PROFILE = os.environ.get('PROFILE', False)

redis_host = '10.239.26.211'
redis_port = 6379

predictions_endpoint = 'http://127.0.0.1:5000/prediction'