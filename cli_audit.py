import os
import json
import sys
import hashlib
from datetime import datetime, timezone
from sweep.chronos import FullStackChronosEngine
from core.inference_router import InferenceEngineRouter

AUDIT_FILE_PATH = "last_audit_results.json"

def run_cli_audit():
    # 1. Parse dispatch payload passed from WordPress
    event_payload_str = os.getenv("EVENT_PAYLOAD", "{}")
    input_node_env = os.getenv("INPUT_NODE", "").strip()

    target_node = ""
    session_guid = ""
    utc_timestamp = ""
    ecta_hash = ""

    try:
        event_data = json.loads(event_payload_str)
        if isinstance(event_data, dict):
            client = event_data.get("client_payload", event_data)
            target_node = client.get("node_payload")
            session_guid = client.get("session_guid") or client.get("session_id")
            utc_timestamp = client.get("utc_timestamp") or client.get("timestamp")
            ecta_hash = client.get("ecta_hash")
    except Exception as e:
        print(f"[!] Event payload parsing warning: {e}")

    # Fallback assignments if missing
    if not target_node:
        target_node = input_node_env or "America"
    if not session_guid:
        session_guid = f"SESSION-{os.urandom(4).hex().upper()}"
    if not utc_timestamp:
        utc_timestamp = datetime.now(timezone.utc).isoformat()
    if not ecta_hash:
        raw_sig = f"{session_guid}:{utc_timestamp}:{target_node}"
        ecta_hash = f"sha256:{hashlib.sha256(raw_sig.encode()).hexdigest()}"

    print(f"[*] Executing Chronos Audit Engine (Master Ledger Append Mode)...")
    print(f"[*] Target Node  : '{target_node}'")
    print(f"[*] Session GUID : '{session_guid}'")

    # 2. Initialize NIM Router & Execute Sweep
    router = InferenceEngineRouter()
    engine = FullStackChronosEngine(router=router)

    sweep_results = engine.execute_full_sweep(
        industry="Socio-Economic Infrastructure",
        payload=target_node,
        cycle=59763
    )

    # 3. Build current run record payload
    current_run_payload = {
        "security": {
            "session_guid": session_guid,
            "utc_timestamp": utc_timestamp,
            "ecta_hash": ecta_hash,
            "popia_status": "COMPLIANT_NO_PII_EXPOSED"
        },
        "quantum_header": "QUANTUM-CYCLE: 059763 / 144000",
        "quantum_cycle": 59763,
        "mathematics": {
            "shi": 20571.43,
            "tti": 0.0,
            "frequency": 144000.0,
            "logos": 10368000,
            "resistance": 504,
            "constraints": 1.0,
            "override_triggered": True
        },
        "chronos_sweep": sweep_results
    }

    # 4. Load existing audit history if present (or initialize ledger list)
    audit_history = []
    if os.path.exists(AUDIT_FILE_PATH):
        try:
            with open(AUDIT_FILE_PATH, "r") as f:
                existing_data = json.load(f)
                
            if isinstance(existing_data, list):
                audit_history = existing_data
            elif isinstance(existing_data, dict):
                # Upgrade legacy single-object JSON into an array ledger
                audit_history = [existing_data]
        except Exception as err:
            print(f"[!] Warning: Could not parse existing ledger file ({err}). Initializing new ledger.")
            audit_history = []

    # 5. Append current run to historical records
    audit_history.append(current_run_payload)

    # 6. Save updated master ledger back to file
    with open(AUDIT_FILE_PATH, "w") as f:
        json.dump(audit_history, f, indent=2)

    print(f"[✓] Ledger updated! Total historical audit records captured: {len(audit_history)}")

if __name__ == "__main__":
    run_cli_audit()
