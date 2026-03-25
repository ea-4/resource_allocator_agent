from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template

# Worker agent evaluates tasks and proposes utility
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
                task_size = 5
                if self.agent.current_load + task_size <= self.agent.capacity:
                    execution_time = task_size / self.agent.speed
                    utility = execution_time + self.agent.current_load
                    reply = msg.make_reply()
                    reply.set_metadata("performative", "propose")
                    reply.body = str(utility)
                    await self.send(reply)
                    self.agent.current_load += task_size
                    await asyncio.sleep(execution_time)
                    self.agent.current_load -= task_size
                else:
                    print(f"{self.agent.name} -> REFUSE (over capacity)")

    async def setup(self):
        template = Template()
        template.set_metadata("performative", "cfp")
        self.add_behaviour(self.ReceiveCFPBehaviour(), template)
