import os
import json
import sys
from sweep.chronos import FullStackChronosEngine
from core.inference_router import InferenceEngineRouter

def run_cli_audit():
    # 1. Parse trigger metadata passed from WordPress/GitHub event
    event_payload_str = os.getenv("EVENT_PAYLOAD", "{}")
    input_node = os.getenv("INPUT_NODE", "")

    session_id = "default_session"
    target_node = "South Africa"

    try:
        event_data = json.loads(event_payload_str)
        client_payload = event_data.get("client_payload", {})
        
        target_node = client_payload.get("node_payload") or input_node or "South Africa"
        session_id = client_payload.get("session_id") or "default_session"
    except Exception as e:
        print(f"[!] Warning: Could not parse event payload ({e}). Falling back to defaults.")

    print(f"[*] Initializing Chronos Calculus Execution...")
    print(f"[*] Target Node: '{target_node}'")
    print(f"[*] Session ID : '{session_id}'")

    # 2. Initialize NVIDIA NIM AI Router & Engine
    router = InferenceEngineRouter()
    engine = FullStackChronosEngine(router=router)

    # 3. Execute 4,000-Year Sweep (1000 BCE to 3000 CE)
    sweep_results = engine.execute_full_sweep(
        industry="Socio-Economic Infrastructure",
        payload=target_node,
        cycle=59763
    )

    # 4. Construct Final Payload Wrapper
    final_output_payload = {
        "security": {
            "session_guid": session_id,
            "utc_timestamp": os.getenv("GITHUB_RUN_ID", "2026-07-21T12:00:00Z")
        },
        "quantum_header": "QUANTUM-CYCLE: 059763 / 144000",
        "quantum_cycle": 59763,
        "chronos_sweep": sweep_results
    }

    # 5. Save to Isolated Session Path for Multi-User Isolation
    os.makedirs("sessions", exist_ok=True)
    session_file_path = f"sessions/{session_id}.json"
    
    with open(session_file_path, "w") as f:
        json.dump(final_output_payload, f, indent=2)
    print(f"[✓] Session results written to: {session_file_path}")

    # 6. Backward-compatibility output
    with open("last_audit_results.json", "w") as f:
        json.dump(final_output_payload, f, indent=2)
    print(f"[✓] Legacy root results written to: last_audit_results.json")

if __name__ == "__main__":
    run_cli_audit()
