from datetime import datetime, timezone
from config.settings import settings

class QuantumClockEngine:
    """
    Synchronizes 144,000 Quantum Cycles to standard 24-Hour UTC time (1:6000 ratio).
    """
    CYCLES_PER_SECOND = settings.TOTAL_QUANTUM_CYCLES / 86400.0

    @classmethod
    def get_current_cycle(cls) -> int:
        now = datetime.now(timezone.utc)
        elapsed_seconds = (now.hour * 3600) + (now.minute * 60) + now.second + (now.microsecond / 1e6)
        cycle = int(elapsed_seconds * cls.CYCLES_PER_SECOND)
        return min(max(1, cycle), settings.TOTAL_QUANTUM_CYCLES)

    @classmethod
    def get_temporal_header(cls) -> str:
        return f"QUANTUM-CYCLE: {cls.get_current_cycle():06d} / {settings.TOTAL_QUANTUM_CYCLES}"
