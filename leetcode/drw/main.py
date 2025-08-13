"""
Problem Description
You are given N tasks and a runner that can run one task at a time.
Time is modeled as discrete steps starting from 1.
For example, if the time limit C = 4, the timesteps are 1, 2, 3, 4.

At each timestep, the runner can do 1 unit of work.
Each task takes a certain number of time units to run.

Example: Task 1 could take 2 units, Task 2 could take 3 units.
A task is completed when the runner has run it for its full duration.

Constraints:

Tasks cannot be partially completed.

Once a task starts, it must run without interruption until it finishes.

1 ≤ N, C ≤ 1000

Task 1 — Single Runner
Write a function:

Parameters:

tasks — list of integers, where each integer is the total number of time units needed to run that task.

time_limit — integer, the maximum available time units.

Returns:

The maximum number of tasks that can be completed on a single runner within the given time_limit.

"""

def get_max_number_of_completable_tasks(tasks: list[int], time_limit: int) -> int:
    """
    Sort tasks by number of time units needed to run
    Complete shortest task to longest task
    """

    tasks.sort()
    task = 0
    for time in tasks:
        time_limit -= time 
        if time_limit >= 0:
            task += 1
    return task

"""
Task 2 — Two Runners
Now we have two runners (like two CPU cores).
They can run two tasks in parallel, each working on a separate task at the same time.

Returns:

The maximum number of tasks that can be completed on two runners within the given time_limit.
"""

from collections import defaultdict
"""
Naive approach would be to sort the tasks
Then greedily have the 2 workers pick the cheapest task

But this would fail some cases due to internal fragmentation where
total amount of space left in the 2 workers is enough to accomodate a task but the task
cannot fit in any of the workers left over space
"""
def get_max_number_of_completable_tasks_2(tasks: list[int], time_limit: int) -> int:
    # maintain a 2dp array
    # dp[a][b] -> count
    # a represents time used up by runner 1
    # b represents time used up by runner 2
    # count represents number of task completed
    # if we use a dp array we have to make our array time_limit*time_limit which also 
    # contains states that we cannot reach
    # so we can instead use a dp dictionary where we use (a, b) as the keys

    dp = defaultdict(int) # (a, b) -> count

    dp[(0,0)] = 0 
    max_tasks = 0 

    for t in tasks:
        # copy over dictionary where we will update the values
        # so that the changes in states are due to the task
        # and not the previous other states
        new_dp = dp.copy()

        # go through all the previous states
        for (a,b), cnt in dp.items():
            # check if add new task will exceed limit runner 1
            if a + t <= time_limit:
                # create new reachable state
                key = (a+t, b)
                new_dp[key] = max(new_dp[key], cnt+1)
                max_tasks = max(max_tasks, new_dp[key])
            
            # same check for runner 2
            if b + t <= time_limit:
                # create new reachable state
                key = (a, b+t)
                new_dp[key] = max(new_dp[key], cnt+1)
                max_tasks = max(max_tasks, new_dp[key])   

        dp = new_dp

    return max_tasks     

        

