import unittest
from care_edge.demo import ActivityEvent, evaluate

class TestActivityRules(unittest.TestCase):
    def test_sitting_is_not_a_fall(self):
        self.assertEqual(evaluate(ActivityEvent("sim", "2026-01-01T00:00:00Z", "sitting", 0.99)), "no_alert")

    def test_suspected_fall_requests_human_check(self):
        self.assertIn("caregiver check", evaluate(ActivityEvent("sim", "2026-01-01T00:00:00Z", "possible_fall", 0.95)))

    def test_sensor_fault_requests_human_check(self):
        self.assertIn("sensor_fault", evaluate(ActivityEvent("sim", "2026-01-01T00:00:00Z", "sitting", 0.99, "offline")))

if __name__ == "__main__":
    unittest.main()
