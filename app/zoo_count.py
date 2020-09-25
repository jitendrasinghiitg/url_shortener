from kazoo.client import KazooClient
import random
import os

counters_range = {
    "/tiny_id_0": 1,
    "/tiny_id_1": 100000000,
    "/tiny_id_2": 200000000,
    "/tiny_id_3": 300000000,
    "/tiny_id_4": 400000000,
    "/tiny_id_5": 500000000,
    "/tiny_id_6": 600000000,
    "/tiny_id_7": 700000000,
    "/tiny_id_8": 800000000,
    "/tiny_id_9": 900000000
}


def counter():
    zk = KazooClient(hosts=os.getenv("ZOOKEEPER_URL"))
    print("connected with zookeeper")
    zk.start()
    zk.add_listener(lambda zk_state: print(zk_state))
    counter_range = random.sample(counters_range.keys(), 1)[0]
    counter = zk.Counter(counter_range, default=counters_range[counter_range])
    counter += 1
    return counter.pre_value + 1
