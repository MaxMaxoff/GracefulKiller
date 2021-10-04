#!/.venv/bin/python

import signal
from threading import Event


class KillerEvent(Event):
    def __nonzero__(self):
        return self.is_set()
    
    def __len__(self):
        return self.is_set()

# process SIGTERM and SIGINT signals gracefully
class GracefulKiller:
    def __init__(self):
        self.kill_now = KillerEvent()
        for sig in ('TERM', 'HUP', 'INT'):
            signal.signal(getattr(signal, 'SIG' + sig), self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now.set()
