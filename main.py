async def main():
    coordinator = CoordinatorAgent("coordinator@localhost", "password")
    worker = WorkerAgent("worker@localhost", "password", capacity=10, speed=2)

    await coordinator.start()
    await worker.start()

    await asyncio.sleep(20)

    await coordinator.stop()
    await worker.stop()

asyncio.run(main())
