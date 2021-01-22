from collections import Counter
class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        task_count = Counter(tasks)
        most_task = task_count.most_common()
        most_count = most_task[0][1]
        most_frequent_tasks = 0
        for i in task_count.values():
            if i == most_count:
                most_frequent_tasks += 1
        result = (n+1) * (most_count-1) + most_frequent_tasks
        return max(result, len(tasks))
        
