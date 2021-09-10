import redis
from random import randint
import os


def main(_event, _context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    redis_host = os.environ.get('REDIS_HOST', 'localhost')
    redis_port = int(os.environ.get('REDIS_PORT', 6379))
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port)

    ids = [randint(1,1000) for _ in range(10)]
    #ids = list(range(1000))
    print(ids)
    redis_client.delete("online")
    redis_client.sadd("online", *ids)
    redis_client.exists()

if __name__ == '__main__':
    main(1,2)