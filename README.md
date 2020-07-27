# GracefulKiller #

**GracefulKiller** python3 module for process SIGTERM and SIGINT signals gracefully

## Requirements
* signal (build-in)

## Details ##
### Preparations

Install GracefulKiller using pip:

```bash
$ pip install [--user] gracefulkiller
```

### Usage
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