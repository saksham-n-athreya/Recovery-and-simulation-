
from recovery.recovery import terminate_process

allocation = [
    [1, 0],
    [0, 1],
    [1, 1]
]

available = [1, 0]

terminated = [False, False, False]

# Terminate P2 (index 1)
available, allocation, terminated = terminate_process(
    1, allocation, available, terminated
)

print("Available Resources:", available)
print("Allocation Matrix:", allocation)
print("Terminated Processes:", terminated)



from recovery.recovery import terminate_all_deadlocked

allocation = [
    [1, 0],
    [0, 1],
    [1, 1]
]

available = [1, 0]
terminated = [False, False, False]

deadlocked_processes = [0, 2]

available, allocation, terminated = terminate_all_deadlocked(
    deadlocked_processes,
    allocation,
    available,
    terminated
)

print("Available:", available)
print("Allocation:", allocation)
print("Terminated:", terminated)



from recovery.recovery import select_victim

allocation = [
    [2, 1],
    [1, 0],
    [3, 2]
]

terminated = [False, False, False]

deadlocked_processes = [0, 1, 2]

victim = select_victim(
    deadlocked_processes,
    allocation,
    terminated
)

print("Selected victim: P", victim)



from recovery.recovery import automatic_recovery

allocation = [
    [2, 1],
    [1, 0],
    [3, 2]
]

available = [0, 0]
terminated = [False, False, False]

deadlocked_processes = [0, 1, 2]

available, allocation, terminated, log = automatic_recovery(
    deadlocked_processes,
    allocation,
    available,
    terminated
)

print("Available:", available)
print("Terminated:", terminated)
print("Recovery Log:", log)
