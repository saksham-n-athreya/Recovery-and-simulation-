
from datetime import datetime

history = []


def log_event(event_type, description, status="INFO"):
    """
    Records an event in the simulation history.
    """

    event = {
        "step": len(history) + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event_type": event_type,
        "description": description,
        "status": status
    }

    history.append(event)

    return event


def get_history():
    """
    Returns all recorded simulation events.
    """
    return history.copy()


def clear_history():
    """
    Clears the simulation history.
    """
    history.clear()
