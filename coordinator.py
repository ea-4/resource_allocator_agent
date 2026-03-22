import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message


class CoordinatorAgent(Agent):

    class SendCFPBehaviour(OneShotBehaviour):
        async def run(self):
            print("Coordinator: Sending CFP...")

            msg = Message(to="worker@localhost")  # Worker JID
            msg.set_metadata("performative", "cfp")
            msg.body = "task_1"

            await self.send(msg)

    class ReceiveProposalsBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)
            if msg:
                print(f"Coordinator: Received proposal -> {msg.body}")
            else:
                print("Coordinator: No proposals received")
                self.kill()

    async def setup(self):
        print("Coordinator started")
        self.add_behaviour(self.SendCFPBehaviour())
        self.add_behaviour(self.ReceiveProposalsBehaviour())
