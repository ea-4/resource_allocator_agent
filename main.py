from coordinator import CoordinatorAgent 
from worker import WorkerAgent
import os 
import asyncio

async def main():

    
    jid = os.getenv("AGENT_JID")
    jpsw = os.getenv("AGENT_PSW")
    coordinator = CoordinatorAgent("co.a@xmpp.jp", "coordinatorpswd")
    worker = WorkerAgent("w.1@xmpp.jp", "workerpswd", capacity=10, speed=2)


    await coordinator.start()
    await worker.start()


    await asyncio.sleep(20)

    await coordinator.stop()
    await worker.stop()

asyncio.run(main())
