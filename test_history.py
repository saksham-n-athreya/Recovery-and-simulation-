
from history.history import log_event, get_history, clear_history

log_event("START", "Simulation started")
log_event("DETECTION", "Deadlock detected", "WARNING")
log_event("RECOVERY", "Process P1 terminated", "SUCCESS")
log_event("END", "Simulation completed")

for event in get_history():
    print(event)

print("\nTotal Events:", len(get_history()))

clear_history()

print("Events after clearing:", len(get_history()))
