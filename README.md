# Concurrency & parallelism with asyncio & multiprocessing.

### Uses python asyncio & multiprocessing to run a very heavy operation on N CPU cores.

## before rocket ship launch:
![before launch](https://github.com/sergeimellow/python_rocket_ship/blob/master/before_launch.png)

## after rocket ship launch:
![after launch](https://github.com/sergeimellow/python_rocket_ship/blob/master/after_launch.png)

example run
```
$ python python_rocket_ship.py 16
03:50:47 ~/work/python_rocket_ship  $ python python_rocket_ship.py 16
kicking off process # 0
kicking off process # 1
kicking off process # 2
kicking off process # 3
kicking off process # 4
kicking off process # 5
kicking off process # 6
kicking off process # 7
kicking off process # 8
kicking off process # 9
kicking off process # 10
kicking off process # 11
kicking off process # 12
kicking off process # 13
kicking off process # 14
kicking off process # 15
running task one for process 0
running task one for process 1
running task one for process 2
running task one for process 3
running task one for process 4
running task one for process 5
running task one for process 6
running task one for process 7
running task one for process 8
running task one for process 9
running task one for process 10
running task one for process 11
running task one for process 12
running task one for process 13
running task one for process 14
running task one for process 15
... and we hang here while we watch our CPUs go to Mars until we decide they had enough and we ctrl+c the script
```