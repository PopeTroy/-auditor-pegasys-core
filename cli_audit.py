import os
import json
import sys
from core.compliance import ComplianceSession
from core.quantum_clock import QuantumClockEngine
from core.inference_router import InferenceEngineRouter
from core.prophetic_calculator import PropheticCalculatorEngine
from sweep.chronos import FullStackChronosEngine

def main():
    # Parse inputs from environment
    raw_payload = os.environ.get('EVENT_PAYLOAD')
    event_data = {}
    if raw_payload and raw_payload != 'null':
        try:
            parsed = json.loads(raw_payload)
            if isinstance(parsed, dict):
                event_data = parsed
        except Exception:
            event_data = {}

    alias = event_data.get('alias') or os.environ.get('INPUT_ALIAS') or 'Shinobi_User'
    location = event_data.get('location') or os.environ.get('INPUT_LOCATION') or 'South Africa'
    industry = event_data.get('industry') or os.environ.get('INPUT_INDUSTRY') or 'Energy Infrastructure'
    payload = event_data.get('payload') or os.environ.get('INPUT_PAYLOAD') or 'Systemic Friction Node'

    print(f"=== [STARTING PEGASYS AUDIT] ===")
    print(f"User Alias : {alias}")
    print(f"Location   : {location}")
    print(f"Industry   : {industry}")
    print(f"Payload    : {payload}\n")

    # 1. Security & Clock
    session = ComplianceSession(alias)
    token = session.generate_ecta_token(payload)
    q_cycle = QuantumClockEngine.get_current_cycle()
    q_header = QuantumClockEngine.get_temporal_header()
    math_results = PropheticCalculatorEngine.solve_synthesis()

    print(f"[TEMPORAL LOCK] {q_header}")
    print(f"[SHI MATH] SHI = {math_results['shi']} | TTI = {math_results['tti']} | Freq = {math_results['frequency']} Hz\n")

    # 2. Chronos Deep Sweep
    print(f"[EXECUTING 10 SENTINEL SWEEP (1000 BCE - 3000 CE)...]")
    router = InferenceEngineRouter()
    chronos = FullStackChronosEngine(router)
    sweep_results = chronos.execute_full_sweep(industry, payload, q_cycle)

    print("\n=== [REASONING & SWEEP RESULTS] ===")
    for i, res in enumerate(sweep_results, 1):
        print(f"Sentinel-{i:02d} | Epoch: {res.get('epoch')} | Demon: {res.get('demon')} | Angel: {res.get('angel')}")
        print(f"  Friction: {res.get('origin')}")
        print(f"  Outcome : {res.get('outcome')}\n")

    # 3. Output JSON
    output_data = {
        'security': token,
        'quantum_header': q_header,
        'quantum_cycle': q_cycle,
        'mathematics': math_results,
        'chronos_sweep': sweep_results
    }

    with open('last_audit_results.json', 'w') as f:
        json.dump(output_data, f, indent=2)

    print("=== [AUDIT COMPLETE: last_audit_results.json WRITTEN] ===")
    sys.exit(0) # Force immediate exit

if __name__ == "__main__":
    main()
