#!/.venv/bin/python
import signal
import threading
import time
from threading import Event


class KillerEvent(Event):
    def __nonzero__(self):
        return self.is_set()

    def __len__(self):
        return self.is_set()


# process SIGTERM and SIGINT signals gracefully
class GracefulKiller:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GracefulKiller, cls).__new__(cls)
        return cls.instance

    def __init__(self, shutdown_handler):
        assert callable(shutdown_handler)
        self.shutdown_handler = shutdown_handler
        self.kill_now = KillerEvent()
        for sig in ('TERM', 'HUP', 'INT'):
            signalnum = getattr(signal, 'SIG' + sig, None)
            if signalnum is None:
                continue
            signal.signal(signalnum, self.exit_gracefully)

    def kill(self):
        self.kill_now.set()

    def exit_gracefully(self, signum, frame):
        self.kill()

    def shutdown(self):
        if self.shutdown_handler:
            self.shutdown_handler()


class Loop:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Loop, cls).__new__(cls)
        return cls.instance

    def __init__(self, killer, delay):
        assert killer is not None and isinstance(killer, GracefulKiller)
        if delay is None:
            self.delay = 1
        assert isinstance(delay, (int, float))
        self.killer = killer
        self.delay = delay

    def loop(self):
        while True:
            if not self.killer.kill_now:
                time.sleep(self.delay)
                continue
            break
        self.killer.shutdown()

    def start(self):
        threading.Thread(target=self.loop, name="Thread-Loop").start()




