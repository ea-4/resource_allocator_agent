import time
class WorkerAgent:
    def __init__(self, name, capacity, speed):
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.current_load = 0

    def evaluate_task(self, task_size):
        # Check capacity constraint
        if self.current_load + task_size > self.capacity:
            print(f"{self.name} -> REFUSE (over capacity)")
            return None  # No proposal

        execution_time = task_size / self.speed
        load_penalty = self.current_load
        utility = execution_time + load_penalty

        return utility


    def execute_task(self, task_size):
        print(f"{self.name}: Executing task...")
        self.current_load += task_size
        print(f"{self.name}: New load = {self.current_load}")

        execution_time = task_size / self.speed
        time.sleep(execution_time)

        self.current_load -= task_size
        print(f"{self.name}: Task completed. Load now {self.current_load}")
