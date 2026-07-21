import os
import json
import sys
from sweep.chronos import FullStackChronosEngine
from core.inference_router import InferenceEngineRouter

def run_cli_audit():
    # Parse payload sent via GitHub repository dispatch event
    event_payload_str = os.getenv("EVENT_PAYLOAD", "{}")
    input_node_env = os.getenv("INPUT_NODE", "").strip()

    target_node = ""
    session_id = ""

    try:
        event_data = json.loads(event_payload_str)
        
        # Extract direct properties from github.event.client_payload
        if isinstance(event_data, dict):
            target_node = event_data.get("node_payload") or event_data.get("client_payload", {}).get("node_payload")
            session_id = event_data.get("session_id") or event_data.get("client_payload", {}).get("session_id")
    except Exception as e:
        print(f"[!] Warning: Payload JSON parsing error: {e}")

    # Fall back to workflow input environment variables if event dict parsing is empty
    if not target_node:
        target_node = input_node_env
    if not session_id:
        session_id = os.getenv("INPUT_SESSION_ID", "session_standalone")

    # Ensure execution halts if no target subject was supplied from WordPress
    if not target_node:
        print("[X] Critical Error: No target node subject provided from WordPress input. Aborting sweep.")
        sys.exit(1)

    print(f"[*] Starting Chronos Calculus Engine...")
    print(f"[*] Active Session ID: '{session_id}'")
    print(f"[*] Target Node     : '{target_node}'")

    # Initialize NIM AI Router & Chronos Engine
    router = InferenceEngineRouter()
    engine = FullStackChronosEngine(router=router)

    # Execute 4,000-Year Sweep (1000 BCE to 3000 CE)
    sweep_results = engine.execute_full_sweep(
        industry="Socio-Economic Infrastructure",
        payload=target_node,
        cycle=59763
    )

    # Construct Final JSON Payload
    final_output_payload = {
        "security": {
            "session_guid": session_id,
            "utc_timestamp": os.getenv("GITHUB_RUN_ID", "")
        },
        "quantum_header": "QUANTUM-CYCLE: 059763 / 144000",
        "quantum_cycle": 59763,
        "chronos_sweep": sweep_results
    }

    # Save to isolated session file for multi-user isolation
    os.makedirs("sessions", exist_ok=True)
    session_file_path = f"sessions/{session_id}.json"
    
    with open(session_file_path, "w") as f:
        json.dump(final_output_payload, f, indent=2)
    print(f"[✓] Session isolated file successfully created: {session_file_path}")

    # Legacy output file update
    with open("last_audit_results.json", "w") as f:
        json.dump(final_output_payload, f, indent=2)

if __name__ == "__main__":
    run_cli_audit()
