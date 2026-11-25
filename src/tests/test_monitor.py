import unittest
from src.monitor import ServiceStatus, evaluate_services


class TestMonitor(unittest.TestCase):
    def test_all_healthy(self):
        services = [ServiceStatus("API", 20, True), ServiceStatus("DB", 15, True)]
        self.assertTrue(evaluate_services(services))

    def test_degraded_system(self):
        services = [ServiceStatus("API", 20, True), ServiceStatus("Cache", 999, False)]
        self.assertFalse(evaluate_services(services))


if __name__ == "__main__":
    unittest.main()
