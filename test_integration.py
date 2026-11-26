
from recovery.recovery import automatic_recovery
from history.history import get_history, clear_history

allocation = [
    [2, 1],
    [1, 0],
    [3, 2]
]

available = [0, 0]
terminated = [False, False, False]
deadlocked_processes = [0, 1, 2]

clear_history()

available, allocation, terminated, log = automatic_recovery(
    deadlocked_processes,
    allocation,
    available,
    terminated
)

print("Available Resources:", available)
print("Terminated Processes:", terminated)

print("\nSIMULATION HISTORY")

for event in get_history():
    print(event)
