import os
from langchain_groq import ChatGroq

DEFAULT_GROQ_KEY = os.getenv("GROQ_API_KEY", "")

def get_llm_instance(api_key: str = None):
    """
    Returns an LLM instance configured for Groq.
    Uses 'openai/gpt-oss-120b' model on Groq.
    """
    key_to_use = api_key.strip() if api_key and api_key.strip() else DEFAULT_GROQ_KEY
    
    if not key_to_use:
        raise ValueError("Groq API Key missing! Please provide a valid Groq API key.")
        
    return ChatGroq(
        groq_api_key=key_to_use,
        model_name="openai/gpt-oss-120b",
        temperature=0.2
    )
