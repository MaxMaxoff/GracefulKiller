import time
import unittest
from GracefulKiller import GracefulKiller, ThreadLoop, GeventLoop

def shutdown_handler():
    print("shutdown")


class LoopTestCase(unittest.TestCase):

    def test_thread_loop(self):
        killer = GracefulKiller(shutdown_handler)
        ThreadLoop(killer, 1).start()
        time.sleep(3)
        killer.kill()

    def test_gevent_loop(self):
        killer = GracefulKiller(shutdown_handler)
        GeventLoop(killer, 1).start()
        time.sleep(3)
        killer.kill()


if __name__ == "__main__":
    unittest.main()
