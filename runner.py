import time
from dataclasses import dataclass


@dataclass
class RunnerResult:
    id: str
    value: str


def run() -> RunnerResult:
    start_time = time.perf_counter()
    for _ in range(1000):
        pass
    end_time = time.perf_counter()
    print(f"Execution time: {end_time-start_time}")
    return RunnerResult(
        id=f"execution_{int(time.time())}", value=f"{int(time.time() * 1000)}"
    )
