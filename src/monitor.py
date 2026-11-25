from dataclasses import dataclass
from typing import List


@dataclass
class ServiceStatus:
    name: str
    latency_ms: int
    healthy: bool

    def summary(self) -> str:
        state = "ONLINE" if self.healthy else "OFFLINE"
        return f"[{state}] {self.name} ({self.latency_ms}ms)"


def evaluate_services(services: List[ServiceStatus]) -> bool:
    return all(service.healthy for service in services)


if __name__ == "__main__":
    checks = [
        ServiceStatus("Auth API", 42, True),
        ServiceStatus("Database Primary", 18, True),
    ]
    for item in checks:
        print(item.summary())
