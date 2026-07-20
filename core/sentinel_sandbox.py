import uuid

class EphemeralSentinelSandbox:
    def __init__(self, industry: str, index: int, cycle: int):
        self.sandbox_id = f"sentinel-{industry.lower()[:3]}-c{index:02d}-{uuid.uuid4().hex[:6]}"
        self.industry = industry
        self.index = index
        self.cycle = cycle
        self.active = False

    def spin_up(self):
        self.active = True

    def execute(self, payload: dict) -> dict:
        if not self.active:
            raise RuntimeError(f"Sandbox {self.sandbox_id} is inactive.")
        return {"sandbox_id": self.sandbox_id, "status": "EXECUTED", "data": payload}

    def destroy(self):
        self.active = False


class SandboxManagerPool:
    def __init__(self, industry: str, count: int = 10):
        self.industry = industry
        self.count = count

    def run_sandbox_sweep(self, cycle: int, runner_fn) -> list:
        sandboxes = [EphemeralSentinelSandbox(self.industry, i + 1, cycle) for i in range(self.count)]
        results = []
        try:
            for sb in sandboxes:
                sb.spin_up()
            for idx, sb in enumerate(sandboxes):
                res = runner_fn(sb, idx)
                results.append(res)
        finally:
            for sb in sandboxes:
                sb.destroy()
        return results
