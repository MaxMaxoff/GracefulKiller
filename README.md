# GracefulKiller #

**GracefulKiller** python3 module for process SIGTERM, SIGHUP and SIGINT signals gracefully

## Requirements ##

* signal (build-in)

## Details ##

### Preparations ###

Install GracefulKiller using pip:

```bash
pip install [--user] gracefulkiller
```

### Usage ###

Import module:

```python
from GracefulKiller import GracefulKiller
```

Example 1

```python
# import module
from GracefulKiller import GracefulKiller

# create killer
killer = GracefulKiller()

# create loop using killer, will exit from loop if SIGTERM or SIGINT received
while not killer.kill_now:
    # do stuff
```

Example 2

```python
# import module
from GracefulKiller import GracefulKiller

# create killer
killer = GracefulKiller()

# use it as check for SIGTERM and SIGINT
if killer.kill_now:
    sys.exit()
```

Example 3

```python
# import module
from GracefulKiller import GracefulKiller, ThreadLoop

def shutdown_handler():
    print("shutdown")
    
# create killer
killer = GracefulKiller(shutdown_handler)

# thread loop
ThreadLoop(killer, 1).start()

```

Example 4

```python
# import module
from GracefulKiller import GracefulKiller, GeventLoop
import gevent 

def shutdown_handler():
    print("shutdown")
    
# create killer
killer = GracefulKiller(shutdown_handler)

# gevent loop
GeventLoop(killer, 1).start()

```