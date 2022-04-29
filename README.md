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

# create while loop using killer, will exit from loop if SIGTERM or SIGINT received
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
from GracefulKiller import GracefulKiller, Loop

# shutdown handler
def shutdown_handler():
    print("shutdown")
    
# create killer with shutdown handler
killer = GracefulKiller(shutdown_handler)

# start killer loop
Loop(killer, 1).start()

```

### Maintainers ###

Special thanks to:

* [williams824](https://github.com/williams824) Pull request #1: [There is no SIGHUP signal under windows](https://github.com/MaxMaxoff/GracefulKiller/pull/1)
* [cuihairu](https://github.com/cuihairu) Pull request #3: [a simple loop](https://github.com/MaxMaxoff/GracefulKiller/pull/3)
