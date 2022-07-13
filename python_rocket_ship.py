import asyncio
import multiprocessing
import argparse

"""
A little POC that kicks of N processes in parallel.
Each process runs two tasks concurrently but not in paralell in an event loop.

Each task tries to calculate 3**1000000000000

The result is your machine will become a rocket ship

see screenshot of htop for before launch:


and after launch:


sample run:

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
... and we hang here while we watch out CPU go to Mars until we decide they had enough and we ctrl+c

"""

async def heavy_operation():
	return 3**1000000000000

async def run_task_one(process_number):
	print("running task one for process", process_number)
	return await heavy_operation()

async def run_task_two(process_number):
	print("running task two for process", process_number)
	return await heavy_operation()

def bootstrap(process_number):
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.gather(run_task_one(process_number), run_task_two(process_number)))

def get_command_line_args():
    parser = argparse.ArgumentParser(description='Turn your machine CPUs into rocket thrusters')
    parser.add_argument('number_of_processes', type=int, help='number of processes to kick off running a strenuous computation')
    return parser.parse_args()

if __name__ == '__main__':
	args = get_command_line_args()

	for process_number in range(args.number_of_processes):
		process = multiprocessing.Process(
			target=bootstrap,
			args=(process_number,)
		)
		print("kicking off process #", process_number)
		process.start()

