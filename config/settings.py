import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    NVIDIA_NIM_API_KEY: str = os.getenv("NVIDIA_NIM_API_KEY", "")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    NVIDIA_NIM_BASE_URL: str = os.getenv("NVIDIA_NIM_BASE_URL", "https://integrate.api.nvidia.com/v1")
    NVIDIA_NIM_MODEL: str = os.getenv("NVIDIA_NIM_MODEL", "meta/llama-3.3-70b-instruct")
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    PREFERRED_ENGINE: str = os.getenv("PREFERRED_ENGINE", "nvidia_nim")
    TOTAL_QUANTUM_CYCLES: int = int(os.getenv("TOTAL_QUANTUM_CYCLES", "144000"))
    SENTINELS_PER_INDUSTRY: int = int(os.getenv("SENTINELS_PER_INDUSTRY", "10"))
    CHRONOS_START_EPOCH: str = os.getenv("CHRONOS_START_EPOCH", "1000 BCE")
    CHRONOS_END_EPOCH: str = os.getenv("CHRONOS_END_EPOCH", "3000 CE")
    ECTA_HMAC_SECRET: str = os.getenv("ECTA_HMAC_SECRET", "PEGASYS_SHINOBI_KEY_2026")

settings = Settings()
