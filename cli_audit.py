import os
import json
import sys
import hashlib
from datetime import datetime, timezone

# Optional imports from your repository structure
try:
    from sweep.chronos import FullStackChronosEngine
    from core.inference_router import InferenceEngineRouter
except ImportError:
    FullStackChronosEngine = None
    InferenceEngineRouter = None

AUDIT_FILE_PATH = "last_audit_results.json"


def generate_node_seed(node_subject: str) -> int:
    """Generates a deterministic numerical seed from the target node string."""
    clean_subject = node_subject.lower().strip()
    hash_digest = hashlib.sha256(clean_subject.encode('utf-8')).hexdigest()
    return int(hash_digest[:16], 16)


def select_unique_node_vectors(target_node: str, count: int = 10):
    """
    Fallback deterministic generator for unique bottlenecks and protocols
    if the external engine is not directly available or relies on static indexing.
    """
    seed = generate_node_seed(target_node)
    
    # Base Goetic Demon Drivers Pool
    demons = [
        ("Bael", "1.665 kHz"), ("Agares", "4.995 kHz"), ("Vassago", "8.325 kHz"),
        ("Gamigin", "11.655 kHz"), ("Marbas", "14.985 kHz"), ("Valefor", "18.315 kHz"),
        ("Amon", "21.645 kHz"), ("Barbatos", "24.975 kHz"), ("Paimon", "28.305 kHz"),
        ("Buer", "31.635 kHz"), ("Gusion", "34.965 kHz"), ("Sitri", "38.295 kHz"),
        ("Beleth", "41.625 kHz"), ("Leraje", "44.955 kHz"), ("Eligos", "48.285 kHz"),
        ("Zepar", "51.615 kHz"), ("Botis", "54.945 kHz"), ("Bathin", "58.275 kHz"),
        ("Sallos", "61.605 kHz"), ("Purson", "64.935 kHz"), ("Morax", "68.265 kHz"),
        ("Ipos", "71.595 kHz"), ("Aim", "74.925 kHz"), ("Naberius", "78.255 kHz")
    ]
    
    # Base Shem Angels Pool
    angels = [
        ("Vehuiah", "Seraphim", "4.045 kHz"), ("Jeliel", "Seraphim", "12.135 kHz"),
        ("Sitael", "Seraphim", "20.225 kHz"), ("Elemiah", "Seraphim", "28.315 kHz"),
        ("Mahasiah", "Seraphim", "36.405 kHz"), ("Lelahel", "Seraphim", "44.495 kHz"),
        ("Achaiah", "Seraphim", "52.585 kHz"), ("Cahetel", "Seraphim", "60.675 kHz"),
        ("Haziel", "Cherubim", "68.765 kHz"), ("Aladiah", "Cherubim", "76.855 kHz"),
        ("Lauviah", "Thrones", "133.488 kHz"), ("Caliel", "Thrones", "141.578 kHz"),
        ("Leuviah", "Thrones", "149.668 kHz"), ("Pahaliah", "Thrones", "157.758 kHz"),
        ("Nelchael", "Thrones", "165.848 kHz"), ("Yeiayel", "Thrones", "173.939 kHz")
    ]

    # Pre-defined systemic bottleneck templates
    bottleneck_templates = [
        "Disaster Emergency Lag", "Airport Customs Extortion", "Industrial Labor Strikes",
        "Fiat Currency Inflation Drag", "Academic Knowledge Paywalls", "Air Freight Carbon Surcharges",
        "Grid Fire Arson Propagation", "Corporate Greenwashing Deception", "Fossil Fuel Monopolization",
        "Border Trade Tariff Inertia", "Port Container Clearance Friction", "Municipal Water Supply Drag",
        "Pharmaceutical Patent Monopolies", "Telecom Spectrum Bandwidth Congestion", "Transit Mesh Disruption"
    ]

    protocol_templates = [
        "Orbital Early-Warning Scanners Deployment", "Zero-Knowledge Biometric Lock Deployment",
        "Automated Profit-Share Ledger Deployment", "Logos Asset-Backed Currency Deployment",
        "Open Access Universal Vault Deployment", "Hydrogen Airship Transit Mesh Deployment",
        "Electro-Thermal Fire Arrays Deployment", "Real-Time Audit Lock Deployment",
        "Decentralized Micro-Grid Nodes Deployment", "Maglev Automated Rail Mesh Deployment"
    ]

    gemstones = [
        "Amber & Chrysoberyl", "Aragonite & Scapolite", "Moonstone & Selenite",
        "Pearl & Mother of Pearl", "White Chalcedony & Opal", "Ulexite & Labradorite",
        "Rhodonite & Pink Tourmaline", "Petalite & Morganite", "Red Jasper & Hematite", "Bloodstone & Garnet"
    ]

    sweep_results = []
    pool_size = len(bottleneck_templates)
    
    # Calculate unique starting offset based on node hash seed
    start_offset = seed % pool_size

    for idx in range(count):
        # Step through index deterministically using prime multipliers for high variance
        b_idx = (start_offset + idx * 7) % pool_size
        d_idx = (start_offset + idx * 3) % len(demons)
        a_idx = (start_offset + idx * 5) % len(angels)
        g_idx = (start_offset + idx * 2) % len(gemstones)
        
        b_id = f"B-{(b_idx + 1):02d}"
        p_id = f"P-{(idx + 1):02d}"
        
        demon_name, demon_freq = demons[d_idx]
        angel_name, angel_choir, angel_freq = angels[a_idx]
        
        # Calculate dynamic crash dates based on node seed offset
        base_year = 2026 + ((seed + idx) % 7)
        crash_schedule = [f"{base_year + (y * 97)}-{(idx % 12) + 1:02d}-12" for y in range(10)]

        sentinel_record = {
            "sandbox_id": f"sentinel-c{idx+1:02d}",
            "status": "EXECUTED",
            "data": {
                "agent_index": idx + 1,
                "chronos_phase": f"Phase {(idx // 3) + 1}: Diagnostic Arc",
                "diagnostic_scope": "Regional / Statutory Policy Friction",
                "target_node_subject": target_node,
                "biblical_apocalyptic_framework": {
                    "apocalyptic_seal": "Fourth Seal: Pale Horse" if idx < 5 else "Fifth Seal: Altar of Martyrs",
                    "sealed_tribe": "Gad" if idx % 2 == 0 else "Asher",
                    "temporal_birth_gate": "March Gate" if idx % 2 == 0 else "April Gate",
                    "church_anchor": "Pergamum" if idx % 2 == 0 else "Thyatira",
                    "base_degree_frequency_khz": f"{82.5 + (idx * 5.0)} kHz",
                    "zone_classification": "STABILIZED GREEN CORRIDOR"
                },
                "bottleneck": {
                    "id": b_id,
                    "name": f"{bottleneck_templates[b_idx]} in {target_node} Context",
                    "active_demon_driver": demon_name,
                    "frequency_khz": demon_freq,
                    "decay_velocity": round(0.666 + (idx * 0.012), 3),
                    "destabilization_constant_floor": 0.666,
                    "predictive_crash_schedule_10_dates_to_3000ce": crash_schedule
                },
                "protocol": {
                    "id": p_id,
                    "name": protocol_templates[idx % len(protocol_templates)],
                    "ruling_shem_angel": angel_name,
                    "celestial_choir": angel_choir,
                    "frequency_khz": angel_freq,
                    "current_restoration_speed": round(0.710 + (idx * 0.02), 3),
                    "equilibrium_target": 1.0,
                    "piezoelectric_gemstone_vector": gemstones[g_idx]
                },
                "real_time_earth_vector": {
                    "applied_speed": f"{round(0.704 - (idx * 0.05), 4)}x acceleration",
                    "application_width_khz": f"{127.0 + (idx * 7.5):.3f} kHz bandwidth",
                    "frequency_shift_to_ultra_green": f"+{40.0 - (idx * 3.2):.3f} kHz shift",
                    "exact_spatial_target": f"{target_node} Spatial Infrastructure Node #{idx+1}"
                },
                "prophetic_summary_3000ce": (
                    f"Chronos Sentinel Node [Regional / Statutory Policy Friction] analyzed '{target_node}'. "
                    f"Under active parameters, {demon_name} ({demon_freq}) causes friction points across predicted failure schedules. "
                    f"Applying {protocol_templates[idx % len(protocol_templates)]} via {gemstones[g_idx]} at {angel_freq} "
                    f"shifts the node into the 90.0-100.0 kHz Ultra Green Corridor, locking the 1.000 Target Unity."
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

    print(f"[*] Executing Chronos Audit Engine (Append-Only Ledger Mode)...")
    print(f"[*] Target Subject : '{target_node}'")
    print(f"[*] Session GUID   : '{session_guid}'")
    print(f"[*] UTC Timestamp  : '{utc_timestamp}'")

    # 2. Run Engine Sweep (Uses full engine if available, or deterministic seeded generator)
    if FullStackChronosEngine and InferenceEngineRouter:
        try:
            router = InferenceEngineRouter()
            engine = FullStackChronosEngine(router=router)
            sweep_results = engine.execute_full_sweep(
                industry="Socio-Economic Infrastructure",
                payload=target_node,
                cycle=59763
            )
        except Exception as err:
            print(f"[!] Engine execution fallback triggered: {err}")
            sweep_results = select_unique_node_vectors(target_node, count=10)
    else:
        sweep_results = select_unique_node_vectors(target_node, count=10)

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
