from openai import OpenAI
from groq import Groq
from config.settings import settings

class InferenceEngineRouter:
    def __init__(self):
        # Strict 10.0s timeout stops hanging
        self.nvidia_client = OpenAI(
            base_url=settings.NVIDIA_NIM_BASE_URL,
            api_key=settings.NVIDIA_NIM_API_KEY,
            timeout=10.0
        ) if settings.NVIDIA_NIM_API_KEY else None

        self.groq_client = Groq(
            api_key=settings.GROQ_API_KEY,
            timeout=10.0
        ) if settings.GROQ_API_KEY else None

    def query(self, system_prompt: str, user_prompt: str, provider: str = None) -> str:
        selected = provider or settings.PREFERRED_ENGINE
        
        if selected == "nvidia_nim" and self.nvidia_client:
            resp = self.nvidia_client.chat.completions.create(
                messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
                model=settings.NVIDIA_NIM_MODEL,
                temperature=0.2,
                max_tokens=512
            )
            return resp.choices[0].message.content
            
        elif self.groq_client:
            resp = self.groq_client.chat.completions.create(
                messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
                model=settings.GROQ_MODEL,
                temperature=0.2,
                max_tokens=512
            )
            return resp.choices[0].message.content

        raise ValueError("No API key available for query execution.")
