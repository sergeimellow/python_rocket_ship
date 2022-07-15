import asyncio
import multiprocessing
import argparse

"""
A little POC that kicks of N processes in parallel.
Each process runs two tasks concurrently but not in paralell in an event loop.

Each task calls a fake "heavy operation" that just prints something and sleeps for
3 seconds in an infinite while loop

The result is your machine runs N processes in paralell of asyncio event loops and 
each event loop runs two tasks concurrently. 

sample run:

$ $ python python_fake_rocket_ship.py 3
kicking off process # 0
kicking off process # 1
kicking off process # 2
running task one for process 0
process_number & caller: 0 run_task_one
running task two for process 0
process_number & caller: 0 run_task_two
running task one for process 1
process_number & caller: 1 run_task_one
running task two for process 1
process_number & caller: 1 run_task_two
running task one for process 2
process_number & caller: 2 run_task_one
running task two for process 2
process_number & caller: 2 run_task_two

# all 6 tasks across 3 processes are sleeping for 3 seconds

process_number & caller: 0 run_task_one
process_number & caller: 0 run_task_two
process_number & caller: 1 run_task_one
process_number & caller: 1 run_task_two
process_number & caller: 2 run_task_one
process_number & caller: 2 run_task_two

# all 6 tasks across 3 processes are sleeping for 3 seconds

process_number & caller: 0 run_task_one
process_number & caller: 0 run_task_two
process_number & caller: 1 run_task_one
process_number & caller: 1 run_task_two
process_number & caller: 2 run_task_one
process_number & caller: 2 run_task_two
.
.
.
"""

# fake rocket thruster because we never get to the completely blocking 3**1000000000000
# the asyncio.sleep(3) actually allows fopr concurrency to occur, see output above.
async def fake_heavy_operation(process_number, caller):
	while True:
		print ("process_number & caller:", process_number, caller )
		await asyncio.sleep(3)
	return 3**1000000000000

async def run_task_one(process_number):
	print("running task one for process", process_number)
	return await fake_heavy_operation(process_number, "run_task_one")

async def run_task_two(process_number):
	print("running task two for process", process_number)
	return await fake_heavy_operation(process_number, "run_task_two")

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

