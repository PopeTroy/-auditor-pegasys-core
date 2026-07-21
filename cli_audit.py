import os
import json
import sys
import hashlib
from datetime import datetime, timezone

# Optional engine imports from your repository structure
try:
    from sweep.chronos import FullStackChronosEngine
    from core.inference_router import InferenceEngineRouter
except ImportError:
    FullStackChronosEngine = None
    InferenceEngineRouter = None

AUDIT_FILE_PATH = "last_audit_results.json"


def generate_adaptive_node_sweep(target_node: str, count: int = 10):
    """
    Generates 10 completely unique, subject-adaptive bottlenecks, protocols, 
    crash schedules, and 3000 CE prophecies dynamically calculated from 
    the target node string.
    """
    clean_node = target_node.strip().title()
    node_hash = hashlib.sha256(clean_node.lower().encode('utf-8')).hexdigest()

    # Dynamic domain friction templates
    domain_frictions = [
        ("Sovereign Debt Default Drag", "Currency Instability Friction"),
        ("Critical Power Grid Strain", "Energy Monopoly Drag"),
        ("Cross-Border Smuggling Inertia", "Port Customs Extortion"),
        ("Telecom Spectrum Congestion", "Knowledge Paywall Drag"),
        ("Agricultural Drought Supply Drag", "Municipal Water Supply Friction"),
        ("Aviation Fuel Surcharge Drag", "Freight Transit Network Lag"),
        ("Municipal Emergency Response Lag", "Grid Fire Arson Risk"),
        ("Central Bank Interest Rate Drag", "Liquidity Freeze Bottleneck"),
        ("Pharmaceutical Patent Inertia", "Healthcare System Monopoly Drag"),
        ("Automated Rail Mesh Friction", "Customs Inspection Delay")
    ]

    # Dynamic remediation protocol templates
    remediations = [
        ("Decentralized Micro-Grid Mesh", "Red Jasper & Hematite"),
        ("Zero-Knowledge Border Security Lock", "Aragonite & Scapolite"),
        ("Logos Asset-Backed Currency Ledger", "Pearl & Mother of Pearl"),
        ("Open-Access Universal Knowledge Vault", "White Chalcedony & Opal"),
        ("Hydrogen Airship Transit Mesh", "Ulexite & Labradorite"),
        ("Electro-Thermal Suppression Arrays", "Rhodonite & Pink Tourmaline"),
        ("Automated Profit-Share Ledger", "Moonstone & Selenite"),
        ("Orbital Early-Warning Scanners", "Amber & Chrysoberyl")
    ]

    demons = [
        ("Bael", "1.665 kHz"), ("Agares", "4.995 kHz"), ("Vassago", "8.325 kHz"),
        ("Gamigin", "11.655 kHz"), ("Marbas", "14.985 kHz"), ("Valefor", "18.315 kHz"),
        ("Botis", "54.945 kHz"), ("Bathin", "58.275 kHz"), ("Sallos", "61.605 kHz"),
        ("Purson", "64.935 kHz"), ("Morax", "68.265 kHz"), ("Ipos", "71.595 kHz"),
        ("Aim", "74.925 kHz"), ("Naberius", "78.255 kHz")
    ]

    angels = [
        ("Vehuiah", "Seraphim", "4.045 kHz"), ("Jeliel", "Seraphim", "12.135 kHz"),
        ("Lauviah", "Thrones", "133.488 kHz"), ("Caliel", "Thrones", "141.578 kHz"),
        ("Leuviah", "Thrones", "149.668 kHz"), ("Pahaliah", "Thrones", "157.758 kHz"),
        ("Nelchael", "Thrones", "165.848 kHz"), ("Yeiayel", "Thrones", "173.939 kHz")
    ]

    sweep_results = []

    for idx in range(count):
        # Derive a cryptographic sub-seed per sentinel index for 100% variance
        sub_hash = hashlib.sha256(f"{node_hash}:{idx}".encode('utf-8')).hexdigest()
        sub_seed = int(sub_hash[:16], 16)

        # Select dynamic parameters
        f_title, _ = domain_frictions[sub_seed % len(domain_frictions)]
        p_title, gemstone = remediations[(sub_seed >> 4) % len(remediations)]
        demon_name, demon_freq = demons[(sub_seed >> 8) % len(demons)]
        angel_name, angel_choir, angel_freq = angels[(sub_seed >> 12) % len(angels)]

        # Dynamically generate unique 10-date failure schedules (2026 - 3000 CE)
        base_year = 2026 + (sub_seed % 12)
        year_step = 75 + ((sub_seed >> 3) % 25)
        crash_dates = [
            f"{base_year + (y * year_step)}-{(sub_seed % 12) + 1:02d}-{(sub_seed % 28) + 1:02d}"
            for y in range(10)
        ]

        # Calculate subject-unique IDs
        b_id = f"B-{(sub_seed % 89) + 10:02d}"
        p_id = f"P-{(sub_seed % 89) + 10:02d}"

        sentinel_record = {
            "sandbox_id": f"sentinel-c{idx+1:02d}",
            "status": "EXECUTED",
            "data": {
                "agent_index": idx + 1,
                "chronos_phase": f"Phase {(idx // 3) + 1}: Diagnostic Arc",
                "diagnostic_scope": "Regional / Statutory Policy Friction",
                "target_node_subject": clean_node,
                "biblical_apocalyptic_framework": {
                    "apocalyptic_seal": "Fourth Seal: Pale Horse" if idx < 5 else "Fifth Seal: Altar of Martyrs",
                    "sealed_tribe": "Judah" if sub_seed % 2 == 0 else "Gad",
                    "temporal_birth_gate": "January Gate" if sub_seed % 2 == 0 else "March Gate",
                    "church_anchor": "Ephesus" if sub_seed % 2 == 0 else "Pergamum",
                    "base_degree_frequency_khz": f"{80.0 + (sub_seed % 35):.1f} kHz",
                    "zone_classification": "STABILIZED GREEN CORRIDOR"
                },
                "bottleneck": {
                    "id": b_id,
                    "name": f"{f_title} in {clean_node} Context",
                    "active_demon_driver": demon_name,
                    "frequency_khz": demon_freq,
                    "decay_velocity": round(0.500 + ((sub_seed % 400) / 1000.0), 3),
                    "destabilization_constant_floor": 0.666,
                    "predictive_crash_schedule_10_dates_to_3000ce": crash_dates
                },
                "protocol": {
                    "id": p_id,
                    "name": f"{clean_node} {p_title} Deployment",
                    "ruling_shem_angel": angel_name,
                    "celestial_choir": angel_choir,
                    "frequency_khz": angel_freq,
                    "current_restoration_speed": round(0.700 + ((sub_seed % 250) / 1000.0), 3),
                    "equilibrium_target": 1.0,
                    "piezoelectric_gemstone_vector": gemstone
                },
                "real_time_earth_vector": {
                    "applied_speed": f"{round(0.400 + ((sub_seed % 500) / 1000.0), 4)}x acceleration",
                    "application_width_khz": f"{110.0 + (sub_seed % 60):.3f} kHz bandwidth",
                    "frequency_shift_to_ultra_green": f"+{20.0 + (sub_seed % 40):.3f} kHz shift",
                    "exact_spatial_target": f"{clean_node} Infrastructure Grid Node #{idx+1}"
                },
                "prophetic_summary_3000ce": (
                    f"Chronos Sentinel Node analyzed '{clean_node}'. Under localized operational friction, "
                    f"{demon_name} ({demon_freq}) causes bottlenecking across 10 predicted failure dates ending {crash_dates[-1]}. "
                    f"Applying {clean_node} {p_title} Deployment via {gemstone} at {angel_freq} shifts the node into the "
                    f"90.0-100.0 kHz Ultra Green Corridor, locking the 1.000 Target Unity."
                )
            }
        }
        sweep_results.append(sentinel_record)

    return sweep_results


def run_cli_audit():
    # 1. Parse dispatch payload passed from WordPress via environment variables
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
        print(f"[!] Payload parse notice: {e}")

    # Fallback assignments if variables are missing
    if not target_node:
        target_node = input_node_env or "America"
    if not session_guid:
        session_guid = f"SESSION-{os.urandom(4).hex().upper()}"
    if not utc_timestamp:
        utc_timestamp = datetime.now(timezone.utc).isoformat()
    if not ecta_hash:
        raw_sig = f"{session_guid}:{utc_timestamp}:{target_node}"
        ecta_hash = f"sha256:{hashlib.sha256(raw_sig.encode()).hexdigest()}"

    print(f"[*] Executing Chronos Audit Engine (Adaptive Node Vector Mode)...")
    print(f"[*] Target Subject : '{target_node}'")
    print(f"[*] Session GUID   : '{session_guid}'")
    print(f"[*] UTC Timestamp  : '{utc_timestamp}'")

    # 2. Run Sweep Generation using Subject-Adaptive Hashing Engine
    sweep_results = generate_adaptive_node_sweep(target_node, count=10)

    # 3. Construct current execution record
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

    # 4. Load existing audit history (or initialize ledger array)
    audit_history = []
    if os.path.exists(AUDIT_FILE_PATH):
        try:
            with open(AUDIT_FILE_PATH, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
                
            if isinstance(existing_data, list):
                audit_history = existing_data
            elif isinstance(existing_data, dict):
                audit_history = [existing_data]
        except Exception as err:
            print(f"[!] Warning reading existing ledger ({err}). Initializing new ledger array.")
            audit_history = []

    # 5. Append current run to historical records
    audit_history.append(current_run_payload)

    # 6. Save master ledger back to file
    with open(AUDIT_FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(audit_history, f, indent=2, ensure_ascii=False)

    print(f"[✓] Success! Master ledger updated in '{AUDIT_FILE_PATH}'. Total historical records: {len(audit_history)}")


if __name__ == "__main__":
    run_cli_audit()
