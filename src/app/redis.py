import redis
import os
import config


redis_host = os.environ.get('REDISHOST', config.redis_host)
redis_port = int(os.environ.get('REDISPORT', config.redis_port))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port)


def online_set():
    #ids = [redis_client.rpop("online") for _ in range(10)]
    ids = redis_client.smembers("online")
    ids = [int(id) for id in ids if id]
    return ids


def cached_call_prediction(f, user_id, ex):
    key = f"prediction_{user_id}"
    if redis_client.exists(key):
        value = redis_client.get(key)
    else:
        value = f(user_id)
        redis_client.set(key, value, ex=ex)
    return float(value)
