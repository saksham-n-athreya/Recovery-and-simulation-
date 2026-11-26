from history.history import log_event

def terminate_process(pid, allocation, available, terminated):
    """
    Terminates a process and releases its allocated resources.

    pid: Process ID (row index)
    allocation: Resource allocation matrix
    available: Currently available resources
    terminated: List tracking terminated processes
    """

    # Check whether the process exists
    if pid < 0 or pid >= len(allocation):
        raise ValueError("Invalid process ID")

    # Prevent terminating the same process twice
    if terminated[pid]:
        raise ValueError("Process already terminated")

    # Release allocated resources
    for j in range(len(available)):
        available[j] += allocation[pid][j]
        allocation[pid][j] = 0

    # Mark process as terminated
    terminated[pid] = True

    return available, allocation, terminated



def terminate_all_deadlocked(deadlocked_processes, allocation,
                             available, terminated):

    """
    Terminates all processes identified as deadlocked.
    """

    for pid in deadlocked_processes:

        if pid < 0 or pid >= len(allocation):
            raise ValueError("Invalid process ID")

        if not terminated[pid]:

            available, allocation, terminated = terminate_process(
                pid, allocation, available, terminated
            )

    return available, allocation, terminated



def select_victim(deadlocked_processes, allocation, terminated):

    """
    Selects a process holding the fewest allocated resources.
    """

    candidates = []

    for pid in deadlocked_processes:

        if not terminated[pid]:

            resource_count = sum(allocation[pid])

            candidates.append((resource_count, pid))

    if not candidates:
        raise ValueError("No eligible process for recovery")

    # Select process with the fewest allocated resources
    victim = min(candidates)[1]

    return victim




def automatic_recovery(deadlocked_processes, allocation,
                       available, terminated):

    recovery_log = []

    log_event(
        "RECOVERY_STARTED",
        "Automatic recovery initiated",
        "INFO"
    )

    while any(not terminated[pid] for pid in deadlocked_processes):

        victim = select_victim(
            deadlocked_processes,
            allocation,
            terminated
        )

        log_event(
            "VICTIM_SELECTED",
            f"Process P{victim} selected for termination",
            "WARNING"
        )

        released = allocation[victim].copy()

        available, allocation, terminated = terminate_process(
            victim,
            allocation,
            available,
            terminated
        )

        log_event(
            "PROCESS_TERMINATED",
            f"Process P{victim} terminated",
            "SUCCESS"
        )

        log_event(
            "RESOURCES_RELEASED",
            f"Process P{victim} released resources: {released}",
            "SUCCESS"
        )

        recovery_log.append({
            "process": victim,
            "released_resources": released
        })

    log_event(
        "RECOVERY_COMPLETED",
        "Automatic recovery completed",
        "SUCCESS"
    )

    return available, allocation, terminated, recovery_log

