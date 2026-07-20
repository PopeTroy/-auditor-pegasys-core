from flask import Flask, request, jsonify
from flask_cors import CORS
from core.compliance import ComplianceSession
from core.quantum_clock import QuantumClockEngine
from core.inference_router import InferenceEngineRouter
from core.prophetic_calculator import PropheticCalculatorEngine
from sweep.chronos import FullStackChronosEngine

app = Flask(__name__)
CORS(app)  # Allows WordPress front-end requests

router = InferenceEngineRouter()
chronos = FullStackChronosEngine(router)

@app.route('/api/audit', methods=['POST'])
def run_audit():
    data = request.json or {}
    alias = data.get('alias', 'WP_User')
    location = data.get('location', 'South Africa')
    industry = data.get('industry', 'Energy Infrastructure')
    payload = data.get('payload', '')

    # 1. POPIA / ECTA Security Lock
    session = ComplianceSession(alias)
    token = session.generate_ecta_token(payload)
    q_cycle = QuantumClockEngine.get_current_cycle()
    q_header = QuantumClockEngine.get_temporal_header()

    # 2. Prophetic Equation Matrix Solve
    math_results = PropheticCalculatorEngine.solve_synthesis()

    # 3. Deploy 10 NVIDIA NIM Sentinel AI Clones in Sandboxes
    sweep_results = chronos.execute_full_sweep(industry, payload, q_cycle)

    return jsonify({
        "security": token,
        "quantum_header": q_header,
        "quantum_cycle": q_cycle,
        "mathematics": math_results,
        "chronos_sweep": sweep_results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
