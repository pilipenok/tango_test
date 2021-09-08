from redis3 import Redis

client = Redis()


def online_set():
    ids = [client.rpop("online") for _ in range(10)]
    ids = [int(id) for id in ids if id]
    return ids
