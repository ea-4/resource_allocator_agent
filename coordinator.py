class CoordinatorAgent:
    def __init__(self, workers):
        self.workers = workers

    def run_auction(self, task_size):
        print("\n CFP: Broadcasting task...\n")

        proposals = []

        # Collect proposals
        for worker in self.workers:
            utility = worker.evaluate_task(task_size)
           
            if utility is not None:
                print(f"{worker.name} -> PROPOSE: {utility}")
                proposals.append((worker, utility))

           
        if not proposals:
            print("No available workers for this task")
            return

        # Select best worker
        best_worker, best_utility = min(proposals, key=lambda x: x[1])

        print(f"\n BEST: {best_worker.name} (utility={best_utility})")

        # Send ACCEPT / REJECT
        for worker, utility in proposals:
            if worker == best_worker:
                print(f"{worker.name} <- ACCEPT_PROPOSAL")
                worker.execute_task(task_size)
            else:
                print(f"{worker.name} <- REJECT_PROPOSAL")


        
        responded_workers = [w for w, _ in proposals]

        for worker in self.workers:
            if worker not in responded_workers:
                print(f"{worker.name} did not respond")

