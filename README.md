The nose config is not pickle-able, making the multiprocesses test loader ignore any additional plugins in the config.

```python test_main.py 1```

> WARNING:root:Running tests with 1 processes

> WARNING:root:Plugin count (before pickle): 5

> WARNING:root:Plugin count (after pickle): 4

> WARNING:root:Plugin was successfully loaded!!!!!

> ----------------------------------------------------------------------

> Ran 1 test in 0.011s


```python test_main.py 2```

> WARNING:root:Running tests with 2 processes

> WARNING:root:Plugin count (before pickle): 6

> WARNING:root:Plugin count (after pickle): 4

> ----------------------------------------------------------------------

> Ran 1 test in 0.011s
