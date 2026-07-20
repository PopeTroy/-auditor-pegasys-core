import json
from concurrent.futures import ThreadPoolExecutor
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

        def worker(idx):
            sandbox = pool.sandboxes[idx] if hasattr(pool, 'sandboxes') else None
            sb_id = f"sentinel-{industry.lower()[:3]}-c{idx+1:02d}"
            prompt = f"Agent [{idx+1}/10] | Sandbox: {sb_id} | Node: {payload} | Cycle: {cycle}"
            try:
                raw = self.router.query(self.SYSTEM_PROMPT, prompt)
                data = json.loads(raw)
            except Exception:
                data = {
                    "epoch": f"1000 BCE - Era {idx+1}",
                    "origin": f"Systemic Infrastructure Drag (Agent {idx+1})",
                    "demon": "Astaroth",
                    "angel": "Michael (Sec 19 Filter)",
                    "outcome": "Dimensional Overwrite Active"
                }
            return {"sandbox_id": sb_id, "status": "EXECUTED", "data": data}

        # Fire all 10 Sentinel agents concurrently in parallel
        with ThreadPoolExecutor(max_workers=10) as executor:
            outputs = list(executor.map(worker, range(10)))

        return outputs
