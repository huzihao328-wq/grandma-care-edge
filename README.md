# Grandma Care Edge

Experimental, offline-first elderly-care monitoring prototype. Not a certified emergency or medical system.

## Planned architecture

RTSP camera → local pose/activity detection → ROS 2 events → independent local safety rules → caregiver notifications.

Optional structured telemetry goes to cloud reasoning; cloud suggestions never directly authorize physical robot actions.

## Initial development milestones

1. Simulated activity event schema and offline safety-rule tests.
2. RTSP ingestion and local YOLO11n/MediaPipe inference.
3. ROS 2 event bridge and FastAPI dashboard.
4. Cloud integration, offline queue, and failover tests.

No personal footage, credentials, or API keys should be committed. Human caregiver oversight is essential.
