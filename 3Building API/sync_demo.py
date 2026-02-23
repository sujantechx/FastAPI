import time
from timeit import default_timer as timer

def run_task(name, second):
    print(f"{name} started at: {timer()}")
    time.sleep(second)
    print(f"{name} finished at: {timer()}")
    
start = timer()
run_task1 = run_task("Task 1", 2)
run_task2 = run_task("Task 2", 3)
run_task3 = run_task("Task 3", 1)
end = timer()
print(f'\n Total time taken: {timer() - start:.2f}s')