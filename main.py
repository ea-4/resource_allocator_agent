import asyncio
from coordinator import CoordinatorAgent
from worker import WorkerAgent

async def main():
    coordinator = CoordinatorAgent("coordinator@xmpp.jp", "coordinator_password")
    worker1 = WorkerAgent("worker1@xmpp.jp", "worker1_password", capacity=10, speed=2)
    worker2 = WorkerAgent("worker2@xmpp.jp", "worker2_password", capacity=8, speed=3)

    await coordinator.start(auto_register=True)
    await worker1.start(auto_register=True)
    await worker2.start(auto_register=True)

    await asyncio.sleep(20)

    await coordinator.stop()
    await worker1.stop()
    await worker2.stop()

asyncio.run(main())
