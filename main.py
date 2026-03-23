from coordinator import CoordinatorAgent 
from worker import WorkerAgent
import os 
import asyncio

async def main():

    
    jid = os.getenv("AGENT_JID")
    jpsw = os.getenv("AGENT_PSW")
    coordinator = CoordinatorAgent("coordinator@space", "coordinatorpswd")
    worker = WorkerAgent("worker1@space", "workerpswd", capacity=10, speed=2)


    await coordinator.start(auto_register=True)
    await worker.start(auto_register=True)


    await asyncio.sleep(20)

    await coordinator.stop()
    await worker.stop()

asyncio.run(main())
