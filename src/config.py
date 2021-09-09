import os

app_name = 'tango'

gcp_project_id = "myproject-311515"
gcp_bigtable_instance_id = "tango-instance"

DEBUG = os.environ.get('DEBUG', False)
PROFILE = os.environ.get('PROFILE', False)

redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = os.environ.get('REDIS_PORT', 6379)

predictions_endpoint = 'http://127.0.0.1:5000/prediction'