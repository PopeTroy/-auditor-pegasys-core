import json
from core.inference_router import InferenceEngineRouter
from core.sentinel_sandbox import SandboxManagerPool
from config.settings import settings

class FullStackChronosEngine:
    SYSTEM_PROMPT = f"""
    You are an Ephemeral Sentinel AI agent for Auditor Pegasys.
    Sweep the target node across timelines from {settings.CHRONOS_START_EPOCH} to {settings.CHRONOS_END_EPOCH}.
    Identify:
    1. Epoch Range
    2. Systemic Friction / Origin
    3. Root Demon (Astaroth, Bael, Mammon, Belial, Abaddon, Asmodeus)
    4. Angel Protocol Filter (Michael, Gabriel, Uriel, Raphael, Metatron)
    5. Projected Systemic Outcome
    Return strictly JSON: {{"epoch": "", "origin": "", "demon": "", "angel": "", "outcome": ""}}
    """

    def __init__(self, router: InferenceEngineRouter):
        self.router = router

    def execute_full_sweep(self, industry: str, payload: str, cycle: int) -> list:
        pool = SandboxManagerPool(industry=industry, count=10)

        def task(sandbox, idx):
            prompt = f"Agent [{idx+1}/10] | Sandbox: {sandbox.sandbox_id} | Node: {payload} | Cycle: {cycle}"
            raw = self.router.query(self.SYSTEM_PROMPT, prompt)
            try:
                data = json.loads(raw)
            except Exception:
                data = {
                    "epoch": f"Epoch-{idx+1}",
                    "origin": "Systemic Drag & Structural Bottleneck",
                    "demon": "Astaroth / Mammon",
                    "angel": "Michael (Sec 19 Filter)",
                    "outcome": "Dimensional Overwrite Required"
                }
            return sandbox.execute(data)

        outputs = pool.run_sandbox_sweep(cycle, task)
        return [item["data"] for item in outputs]
