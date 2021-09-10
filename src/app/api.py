from flask import Blueprint
from app.redis import online_set, cached_call_prediction
from app.db import filtered_online_set
from random import random
import requests
import config
import time


api = Blueprint('api', __name__)


@api.route("/online/<user_id>", methods=['GET', 'POST'])
def online(user_id):
    t = time.time()
    online_ids = online_set()
    ids = filtered_online_set(user_id, online_ids)
    ids = list(ids)
    result = {
        str(id): cached_call_prediction(call_prediction, id, 15)
        for id in ids
    }
    result.update({
        #'online_ids': online_ids,
        'timing': time.time() - t
    })
    return result


def call_prediction(user_id):
    session = requests.Session()
    api_uri = f"{config.prediction_url}/{user_id}"
    resp = session.get(api_uri)
    value = resp.content.decode()
    return value


@api.route("/prediction/<user_id>", methods=['GET'])
def prediction(user_id):
    value = _get_prediction(user_id)
    return str(value)


def _get_prediction(user_id):
    user_id = int(user_id)
    value = random()/user_id if user_id > 0 else 0
    return value
