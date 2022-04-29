import time
import unittest

try:
    from GracefulKiller.GracefulKiller import GracefulKiller, Loop
except:
    from src.GracefulKiller.GracefulKiller import GracefulKiller, Loop
    

def shutdown_handler():
    print("shutdown")


class LoopTestCase(unittest.TestCase):

    def kill(self, killer):
        time.sleep(3)
        killer.kill()

    def test_thread_loop(self):
        killer = GracefulKiller(shutdown_handler)
        Loop(killer, 1).start()
        self.kill(killer)

    def test_create_killer_without_shutdown_handler(self):
        killer = GracefulKiller()
        Loop(killer, 1).start()
        self.kill(killer)



if __name__ == "__main__":
    unittest.main()
