import uuid
import hashlib
import hmac
from datetime import datetime, timezone
from config.settings import settings

class ComplianceSession:
    """
    Enforces POPIA (Act 4 of 2013) user anonymization and ECTA (Act 25 of 2002)
    data message non-repudiation cryptographic verification.
    """
    def __init__(self, user_alias: str):
        self.session_guid = str(uuid.uuid5(uuid.NAMESPACE_DNS, user_alias))
        self.secret_key = settings.ECTA_HMAC_SECRET.encode('utf-8')
        
    def generate_ecta_token(self, payload: str) -> dict:
        utc_now = datetime.now(timezone.utc).isoformat()
        message_bytes = f"{self.session_guid}:{utc_now}:{payload}".encode('utf-8')
        ecta_hash = hmac.new(self.secret_key, message_bytes, hashlib.sha256).hexdigest()
        
        return {
            "session_guid": self.session_guid,
            "utc_timestamp": utc_now,
            "ecta_hash": f"sha256:{ecta_hash}"
        }
