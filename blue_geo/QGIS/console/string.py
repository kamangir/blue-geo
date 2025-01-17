import time
import random


def Q_timestamp():
    return time.strftime(
        f"%Y-%m-%d-%H-%M-%S-{random.randrange(100000):05d}",
        time.localtime(time.time()),
    )
