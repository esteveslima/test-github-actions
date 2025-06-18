import time
from dataclasses import dataclass


@dataclass
class RunnerResult:
    id: str
    value: str


def run() -> RunnerResult:
    return RunnerResult(
        id=f"execution_{int(time.time())}", value=f"{int(time.time() * 1000)}"
    )
