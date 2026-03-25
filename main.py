from coordinator import CoordinatorAgent
from worker import WorkerAgent
from task import Task   # optional

def main():

    # Create workers
    workers = [
        WorkerAgent("Worker1", capacity=10, speed=2),
        WorkerAgent("Worker2", capacity=8, speed=4),
        WorkerAgent("Worker3", capacity=6, speed=1),
    ]

    coordinator = CoordinatorAgent(workers)

    # Define tasks
    tasks = [
        Task("T1", 10),
        Task("T2", 5),
        Task("T3", 8)
    ]

    # Run system
    for task in tasks:
        print(f"\n========== TASK {task.task_id} ==========")
        coordinator.run_auction(task.size)


if __name__ == "__main__":
    main()
