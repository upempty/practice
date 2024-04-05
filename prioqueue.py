import heapq
class PrioTask:
    def __init__(self, prio, name):
        self.prio = prio
        self.name = name
    def __lt__(self, other):
        return self.prio < other.prio

prioTasks = []

heapq.heappush(prioTasks, PrioTask(3, 'lowest prio task'))
heapq.heappush(prioTasks, PrioTask(1, 'highest prio task'))
heapq.heappush(prioTasks, PrioTask(2, 'medium prio task'))

while prioTasks:
    task = heapq.heappop(prioTasks)
    print(f'Executing task:{task.name}, prio: {task.prio}')