"""Simulation-only event processing. Not an emergency response system."""
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class ActivityEvent:
    device_id: str
    timestamp: str
    activity: str
    confidence: float
    sensor_status: str = "healthy"


def evaluate(event: ActivityEvent) -> str:
    if event.sensor_status != "healthy":
        return "sensor_fault: caregiver check requested"
    if event.activity == "possible_fall" and event.confidence >= 0.9:
        return "possible_fall: caregiver check requested"
    return "no_alert"


def main() -> None:
    event = ActivityEvent("simulation", datetime.now(timezone.utc).isoformat(), "sitting", 0.98)
    print(evaluate(event))


if __name__ == "__main__":
    main()
