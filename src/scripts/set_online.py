from time import sleep
from redis import Redis
from random import randint

client = Redis()

while True:
    ids = [randint(1,1000) for _ in range(1000)]
    ids = list(range(1000))
    print(ids)
    client.lpush("online", *ids)
    sleep(10)