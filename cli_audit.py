import os
import json
import sys
from sweep.chronos import FullStackChronosEngine
from core.inference_router import InferenceEngineRouter

def run_cli_audit():
    # Parse payload sent via GitHub repository dispatch
    event_payload_str = os.getenv("EVENT_PAYLOAD", "{}")
    input_node_env = os.getenv("INPUT_NODE", "").strip()

    target_node = ""

    try:
        event_data = json.loads(event_payload_str)
        if isinstance(event_data, dict):
            target_node = event_data.get("node_payload") or event_data.get("client_payload", {}).get("node_payload")
    except Exception as e:
        print(f"[!] Payload parse error: {e}")

    if not target_node:
        target_node = input_node_env or "South Africa"

    print(f"[*] Running Chronos Sweep for Target: '{target_node}'")

    # Initialize NIM Router & Chronos Engine
    router = InferenceEngineRouter()
    engine = FullStackChronosEngine(router=router)

    # Execute 4,000-Year Sweep
    sweep_results = engine.execute_full_sweep(
        industry="Socio-Economic Infrastructure",
        payload=target_node,
        cycle=59763
    )

    # Build Output Structure
    final_output_payload = {
        "quantum_header": "QUANTUM-CYCLE: 059763 / 144000",
        "quantum_cycle": 59763,
        "chronos_sweep": sweep_results
    }

    # Save directly to last_audit_results.json at root
    with open("last_audit_results.json", "w") as f:
        json.dump(final_output_payload, f, indent=2)

    print("[✓] Execution complete. Results written to last_audit_results.json")

if __name__ == "__main__":
    run_cli_audit()
