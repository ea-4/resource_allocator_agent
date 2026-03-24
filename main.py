from coordinator import CoordinatorAgent 
from worker import WorkerAgent
import os 
import asyncio

async def main():

    
    wpswd = os.getenv("W1_PSWD")
    jpswd = os.getenv("COOR_PSWD")
    coordinator = CoordinatorAgent("co.a@localhost", jpswd, use_tls=False, use_ssl=False)
    worker = WorkerAgent("w.1@localhost", wpswd, capacity=10, speed=2, use_tls=False, use_ssl=False)


    await coordinator.start(auto_register=True)
    await worker.start(auto_register=True)

    await asyncio.sleep(5)

    await asyncio.sleep(20)

    await coordinator.stop()
    await worker.stop()

asyncio.run(main())
