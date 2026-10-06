import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    # API Keys & Endpoints
    NVIDIA_NIM_API_KEY: str = os.getenv("NVIDIA_NIM_API_KEY", "")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    NVIDIA_NIM_BASE_URL: str = os.getenv("NVIDIA_NIM_BASE_URL", "https://integrate.api.nvidia.com/v1")
    
    # Defaults
    PREFERRED_ENGINE: str = os.getenv("PREFERRED_ENGINE", "nvidia_nim")
    NVIDIA_NIM_MODEL: str = os.getenv("NVIDIA_NIM_MODEL", "nvidia/nemotron-3-ultra-550b-a55b")
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    
    # -------------------------------------------------------------------------
    # NVIDIA NEMOTRON MODEL SUITE (Reasoning, Omni, Agentic & Parsing)
    # -------------------------------------------------------------------------
    NEMOTRON_3_ULTRA_550B: str = "nvidia/nemotron-3-ultra-550b-a55b"
    NEMOTRON_3_5_LIGHTNING_30B: str = "nvidia/nemotron-3.5-lightning-30b-a3b"
    NEMOTRON_3_SUPER_120B: str = "nvidia/nemotron-3-super-120b-a12b"
    NEMOTRON_3_NANO_OMNI_30B: str = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning"
    
    # Document Intelligence & Clean Text Extraction
    NEMOTRON_PARSE_2_0: str = "nvidia/nemotron-parse-2.0"
    NEMOTRON_OCR_V2: str = "nvidia/nemotron-ocr-v2"
    
    # -------------------------------------------------------------------------
    # GOOGLE MODELS (Gemma Series)
    # -------------------------------------------------------------------------
    GOOGLE_GEMMA_4_31B_IT: str = "google/gemma-4-31b-it"
    GOOGLE_DIFFUSION_GEMMA_26B: str = "google/diffusiongemma-26b-a4b-it"
    
    # -------------------------------------------------------------------------
    # PARAKEET & SPEECH PARSING (Audio / Clean Text Structuring)
    # -------------------------------------------------------------------------
    PARAKEET_TDT_0_6B: str = "nvidia/parakeet-tdt-0.6b"
    PARAKEET_CTC_1_1B: str = "nvidia/parakeet-ctc-1.1b"
    
    # -------------------------------------------------------------------------
    # QWEN & MINIMAX MODELS (Downloadable NIMs)
    # -------------------------------------------------------------------------
    QWEN_2_5_MAX: str = "qwen/qwen2.5-max"
    QWEN_2_5_CODER_32B_INSTRUCT: str = "qwen/qwen2.5-coder-32b-instruct"
    QWEN_IMAGE: str = "qwen/qwen-image"
    MINIMAX_TEXT_01: str = "minimax/minimax-text-01"
    
    # -------------------------------------------------------------------------
    # RAG, EMBEDDING & RERANKING MICROSERVICES
    # -------------------------------------------------------------------------
    NVIDIA_EMBED_QA_4: str = "nvidia/nv-embedqa-e5-v5"
    NEMOTRON_RETRIEVER_EMBED_V1: str = "nvidia/nemotron-retriever-embed-v1"
    NEMOTRON_RETRIEVER_RERANK_V1: str = "nvidia/nemotron-retriever-rerank-v1"
    
    # System Parameters
    TOTAL_QUANTUM_CYCLES: int = int(os.getenv("TOTAL_QUANTUM_CYCLES", "144000"))
    SENTINELS_PER_INDUSTRY: int = int(os.getenv("SENTINELS_PER_INDUSTRY", "10"))
    CHRONOS_START_EPOCH: str = os.getenv("CHRONOS_START_EPOCH", "1000 BCE")
    CHRONOS_END_EPOCH: str = os.getenv("CHRONOS_END_EPOCH", "3000 CE")
    ECTA_HMAC_SECRET: str = os.getenv("ECTA_HMAC_SECRET", "PEGASYS_SHINOBI_KEY_2026")

settings = Settings()
