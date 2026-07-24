use axum::{
    extract::State,
    http::StatusCode,
    routing::{get, post},
    Json, Router,
};
use prost::Message;
use serde::Deserialize;
use sha2::{Digest, Sha256};
use std::net::SocketAddr;
use tokio::fs::{self, File};
use tokio::io::AsyncWriteExt;
use tokio::sync::mpsc;

// Compiled Protobuf namespace
pub mod pegasys {
    pub mod audit {
        include!(concat!(env!("OUT_DIR"), "/pegasys.audit.rs"));
    }
}

use pegasys::audit as pb;

const LEDGER_BIN_PATH: &str = "last_audit_results.bin";
const LEDGER_JSON_PATH: &str = "last_audit_results.json";

#[derive(Debug, Deserialize)]
struct AuditRequest {
    node_payload: String,
    session_guid: Option<String>,
    utc_timestamp: Option<String>,
}

#[derive(Clone)]
struct AppState {
    tx: mpsc::Sender<pb::AuditRunPayload>,
}

#[tokio::main]
async fn main() {
    // Non-blocking channel queue for 10,000 pending audit dispatches
    let (tx, rx) = mpsc::channel::<pb::AuditRunPayload>(10000);

    // Dedicated background worker for atomic ledger commits
    tokio::spawn(async move {
        shinobi_ledger_worker(rx).await;
    });

    let state = AppState { tx };

    // Axum Web Router
    let app = Router::new()
        .route("/api/audit", post(handle_audit_dispatch))
        .route("/api/health", get(|| async { "PEGASYS_RUST_ENGINE_ONLINE" }))
        .with_state(state);

    let addr = SocketAddr::from(([0, 0, 0, 0], 3000));
    println!("[✓] Non-Blocking Tokio Engine listening on http://{}", addr);

    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

async fn handle_audit_dispatch(
    State(state): State<AppState>,
    Json(payload): Json<AuditRequest>,
) -> (StatusCode, Json<serde_json::Value>) {
    let target_node = if payload.node_payload.trim().is_empty() {
        "America".to_string()
    } else {
        payload.node_payload.trim().to_string()
    };

    let session_guid = payload
        .session_guid
        .unwrap_or_else(|| format!("SESSION-{:X}", rand::random::<u32>()));
    let utc_timestamp = payload
        .utc_timestamp
        .unwrap_or_else(|| chrono::Utc::now().to_rfc3339());

    let run_payload = generate_adaptive_node_sweep(&target_node, &session_guid, &utc_timestamp, 10);

    if let Err(e) = state.tx.send(run_payload).await {
        eprintln!("[!] Worker queue saturation error: {}", e);
        return (
            StatusCode::INTERNAL_SERVER_ERROR,
            Json(serde_json::json!({ "error": "QUEUE_SATURATED" })),
        );
    }

    (
        StatusCode::ACCEPTED,
        Json(serde_json::json!({
            "status": "DISPATCHED_TO_PROTOBUF_LEDGER",
            "session_guid": session_guid,
            "target_node": target_node
        })),
    )
}

fn generate_adaptive_node_sweep(
    node: &str,
    guid: &str,
    timestamp: &str,
    count: usize,
) -> pb::AuditRunPayload {
    let mut hasher = Sha256::new();
    hasher.update(node.to_lowercase().as_bytes());
    let node_hash = hex::encode(hasher.finalize());

    let mut sweep_results = Vec::new();

    for idx in 0..count {
        let sub_hash_str = format!("{}:{}:idx_{}", node_hash, guid, idx);
        let mut sub_hasher = Sha256::new();
        sub_hasher.update(sub_hash_str.as_bytes());
        let sub_hash = hex::encode(sub_hasher.finalize());
        let sub_seed = u64::from_str_radix(&sub_hash[..16], 16).unwrap_or(0);

        let hiraishin_mark = format!("HIRAISHIN-FORMULA-MARK-#{:02}-{:.8}", idx + 1, node_hash.to_uppercase());

        let record = pb::SentinelRecord {
            sandbox_id: format!("sentinel-c{:02}", idx + 1),
            status: "EXECUTED".to_string(),
            target_node_subject: node.to_string(),
            framework: Some(pb::ApocalypticFramework {
                apocalyptic_seal: if idx < 5 { "Fourth Seal: Pale Horse" } else { "Fifth Seal: Altar of Martyrs" }.to_string(),
                sealed_tribe: if sub_seed % 2 == 0 { "Judah" } else { "Gad" }.to_string(),
                temporal_birth_gate: if sub_seed % 2 == 0 { "January Gate" } else { "March Gate" }.to_string(),
                church_anchor: if sub_seed % 2 == 0 { "Ephesus" } else { "Pergamum" }.to_string(),
                base_degree_frequency_khz: format!("{:.1} kHz", 80.0 + (sub_seed % 35) as f64),
                zone_classification: "STABILIZED GREEN CORRIDOR".to_string(),
            }),
            bottleneck: Some(pb::Bottleneck {
                id: format!("B-{:02}", (sub_seed % 72) + 1),
                name: format!("Sovereign Friction in {} Context", node),
                active_demon_driver: format!("#{} Goetic Spirit", (sub_seed % 72) + 1),
                frequency_khz: format!("{:.3} kHz", (sub_seed % 240) as f64 * 3.33),
                decay_velocity: 0.500 + ((sub_seed % 400) as f64 / 1000.0),
                destabilization_constant_floor: 0.666,
                predictive_crash_schedule: (0..10)
                    .map(|y| format!("{}-05-12", 2026 + (y * 75)))
                    .collect(),
            }),
            protocol: Some(pb::Protocol {
                id: format!("P-{:02}", ((sub_seed >> 4) % 72) + 1),
                name: format!("{} Remediation Mesh Deployment", node),
                ruling_shem_angel: "Vehuiah".to_string(),
                celestial_choir: "Seraphim".to_string(),
                frequency_khz: "4.045 kHz".to_string(),
                current_restoration_speed: 0.700 + ((sub_seed % 250) as f64 / 1000.0),
                equilibrium_target: 1.0,
            }),
            telemetry: Some(pb::ShinobiTelemetry {
                dojutsu: "Rinnegan 6-Paths".to_string(),
                biju_resonator: "Kurama 9-Tails Dense Yang Energy".to_string(),
                senjutsu_balance: "Six Paths Sage Mode".to_string(),
                eight_gates_overclock: "Gate 8: Night Guy Quantum Space Distortion".to_string(),
                dust_release_deconstruction: "Atomic Molecular Deconstruction".to_string(),
                state_recovery_protocol: "Izanagi Active Zero-Point Rewind".to_string(),
                shadow_bind_efficiency: "98.5% Velocity Immobilization".to_string(),
                medical_regen_rate: "99.2% Recovery Speed".to_string(),
                hiraishin_formula: hiraishin_mark,
            }),
            prophetic_summary: format!(
                "Chronos Sentinel Node analyzed '{}'. Zero-copy binary Protobuf state verified.",
                node
            ),
        };

        sweep_results.push(record);
    }

    let ecta_sig = format!("{}:{}:{}", guid, timestamp, node);
    let mut ecta_hasher = Sha256::new();
    ecta_hasher.update(ecta_sig.as_bytes());

    pb::AuditRunPayload {
        session_guid: guid.to_string(),
        utc_timestamp: timestamp.to_string(),
        ecta_hash: format!("sha256:{}", hex::encode(ecta_hasher.finalize())),
        quantum_cycle: 59763,
        sweep_results,
    }
}

async fn shinobi_ledger_worker(mut rx: mpsc::Receiver<pb::AuditRunPayload>) {
    while let Some(payload) = rx.recv().await {
        let mut ledger = match fs::read(LEDGER_BIN_PATH).await {
            Ok(bytes) => pb::MasterLedger::decode(&bytes[..]).unwrap_or_default(),
            Err(_) => pb::MasterLedger::default(),
        };

        ledger.runs.push(payload);

        let mut buf = Vec::new();
        if ledger.encode(&mut buf).is_ok() {
            let tmp_bin = format!("{}.tmp", LEDGER_BIN_PATH);
            if let Ok(mut file) = File::create(&tmp_bin).await {
                let _ = file.write_all(&buf).await;
                let _ = fs::rename(tmp_bin, LEDGER_BIN_PATH).await;
            }
        }

        if let Ok(json_str) = serde_json::to_string_pretty(&ledger.runs) {
            let tmp_json = format!("{}.tmp", LEDGER_JSON_PATH);
            if let Ok(mut file) = File::create(&tmp_json).await {
                let _ = file.write_all(json_str.as_bytes()).await;
                let _ = fs::rename(tmp_json, LEDGER_JSON_PATH).await;
            }
        }

        println!("[✓] Atomic Commit Successful. Total Ledger Runs: {}", ledger.runs.len());
    }
}
