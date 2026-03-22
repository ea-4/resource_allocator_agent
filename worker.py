class WorkerAgent(Agent):

    def __init__(self, jid, password, capacity, speed):
        super().__init__(jid, password)
        self.capacity = capacity
        self.speed = speed
        self.current_load = 0

    class ReceiveCFPBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)
            if msg:
                print(f"Worker: CFP received -> {msg.body}")

                # Simple evaluation
                execution_time = 10 / self.agent.speed
                load_penalty = self.agent.current_load

                utility = execution_time + load_penalty

                reply = msg.make_reply()
                reply.set_metadata("performative", "propose")
                reply.body = str(utility)

                await self.send(reply)
            else:
                self.kill()

    async def setup(self):
        print("Worker started")
        self.add_behaviour(self.ReceiveCFPBehaviour())
