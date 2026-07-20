import os
import json
import sys
import uuid
import hashlib
from datetime import datetime, timezone

from core.compliance import ComplianceSession
from core.inference_router import InferenceEngineRouter
from core.prophetic_calculator import PropheticCalculatorEngine
from sweep.chronos import FullStackChronosEngine

def calculate_144k_quantum_cycle():
    """
    Computes the exact Quantum Cycle within the 24-hour clock (1:6000 ratio).
    24 Hours = 86,400 Linear UTC Seconds = 144,000 Quantum Cycles.
    1 Linear Second = 1.666667 Quantum Cycles.
    """
    now = datetime.now(timezone.utc)
    seconds_today = (now.hour * 3600) + (now.minute * 60) + now.second + (now.microsecond / 1_000_000.0)
    
    # 1:6000 ratio scaling
    quantum_cycle = int((seconds_today / 86400.0) * 144000)
    return quantum_cycle, now.isoformat()

def main():
    # 1. Extract Single Subject / Node Input
    raw_payload = os.environ.get('EVENT_PAYLOAD')
    node_text = ""
    
    if raw_payload and raw_payload != 'null':
        try:
            parsed = json.loads(raw_payload)
            if isinstance(parsed, dict):
                node_text = parsed.get('node_payload') or parsed.get('payload') or ""
        except Exception:
            node_text = ""

    if not node_text:
        node_text = os.environ.get('INPUT_NODE') or "Unspecified Sovereign Node"

    # 2. Compute 1:6000 Quantum Ratio Clock & Unique POPIA/ECTA Session GUID
    quantum_cycle, utc_iso = calculate_144k_quantum_cycle()
    
    # Generate unique Session GUID seeded by node hash + current micro-cycle
    node_hash = hashlib.sha256(f"{node_text}_{utc_iso}".encode('utf-8')).hexdigest()
    session_guid = str(uuid.uuid5(uuid.NAMESPACE_DNS, node_hash))
    ecta_hash = f"sha256:{node_hash}"

    print(f"=== [AUDITOR PEGASYS SINGLE-NODE HUNT] ===")
    print(f"SESSION GUID   : {session_guid}")
    print(f"TEMPORAL LOCK  : QUANTUM-CYCLE: {quantum_cycle:06d} / 144000")
    print(f"ECTA HASH      : {ecta_hash}")
    print(f"TARGET NODE    : {node_text[:80]}...\n")

    # 3. Prophetic Calculator & Chronos Sweep
    math_results = PropheticCalculatorEngine.solve_synthesis()
    router = InferenceEngineRouter()
    chronos = FullStackChronosEngine(router)
    
    # Pass node text to 10 Sentinels
    sweep_results = chronos.execute_full_sweep("Sovereign Node Diagnostics", node_text, quantum_cycle)

    # 4. Output Clean JSON
    output_data = {
        'security': {
            'session_guid': session_guid,
            'utc_timestamp': utc_iso,
            'ecta_hash': ecta_hash
        },
        'quantum_header': f"QUANTUM-CYCLE: {quantum_cycle:06d} / 144000",
        'quantum_cycle': quantum_cycle,
        'mathematics': math_results,
        'chronos_sweep': sweep_results
    }

    with open('last_audit_results.json', 'w') as f:
        json.dump(output_data, f, indent=2)

    print("=== [AUDIT COMPLETE: UNIQUE NODE RESULTS WRITTEN] ===")
    sys.exit(0)

if __name__ == "__main__":
    main()
