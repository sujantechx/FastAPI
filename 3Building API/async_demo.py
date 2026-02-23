import asyncio 
from os import name
from timeit import default_timer as timer 

async def run_task(name , second):
    
    print(f"{name} started at: {timer()}")
    await asyncio.sleep(second)
    print(f"{name} finshed at: {timer()}")
    

async def main():
    start=timer()
    await asyncio.gather(
        run_task("Task 1", 2),
        run_task("Task 2", 3),
        run_task("Task 3", 1)
    )
    print(f"Main finished at: {timer()}")  # ✅ Correct    
asyncio.run(main())
    
