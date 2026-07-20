from flask import Flask, render_template, request, jsonify
from core.compliance import ComplianceSession
from core.quantum_clock import QuantumClockEngine
from core.inference_router import InferenceEngineRouter
from core.prophetic_calculator import PropheticCalculatorEngine
from sweep.chronos import FullStackChronosEngine
from sweep.regional import RegionalAdjudicationTracker

app = Flask(__name__)
router = InferenceEngineRouter()
chronos = FullStackChronosEngine(router)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/audit', methods=['POST'])
def run_audit():
    data = request.json or {}
    alias = data.get('alias', 'AnonymousUser')
    location = data.get('location', 'South Africa')
    industry = data.get('industry', 'Energy & Grid')
    payload = data.get('payload', 'Systemic Infrastructure Drag')

    # Security & Clock Lock
    session = ComplianceSession(alias)
    token = session.generate_ecta_token(payload)
    q_cycle = QuantumClockEngine.get_current_cycle()
    q_header = QuantumClockEngine.get_temporal_header()

    # Calculations & Sweep
    math_results = PropheticCalculatorEngine.solve_synthesis()
    sweep_results = chronos.execute_full_sweep(industry, payload, q_cycle)
    regional = RegionalAdjudicationTracker.audit_jurisdiction(location)

    return jsonify({
        "security": token,
        "quantum_header": q_header,
        "quantum_cycle": q_cycle,
        "mathematics": math_results,
        "chronos_sweep": sweep_results,
        "regional_adjudication": regional
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
