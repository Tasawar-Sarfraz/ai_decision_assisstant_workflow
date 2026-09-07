import os
from langchain_groq import ChatGroq

# Default API Key from Environment
DEFAULT_GROQ_KEY = os.getenv("GROQ_API_KEY", "")

def get_llm_instance(api_key: str = None):
    """
    Returns a configured LLM instance with dynamic API key support.
    Temperature 0.2 keeps the model strictly logical and prevents hallucination.
    """
    key_to_use = api_key.strip() if api_key and api_key.strip() else DEFAULT_GROQ_KEY
    
    if not key_to_use:
        raise ValueError("Groq API Key nahi mili! Kripya API Key provide karein.")
        
    return ChatGroq(
        groq_api_key=key_to_use,
        model_name="llama-3.1-8b-instant",
        temperature=0.2
    )
