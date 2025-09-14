import os

class Config:
    # Hugging Face API configuration - Using a more powerful model
    HUGGING_FACE_TOKEN = "hf_yUJkVJeecSqbNmjmfpNwyJvltXekSQVwu"
    HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    
    # Tool configuration
    MAX_TOOL_CALLS = 10
    
    # Response formatting
    MAX_RESPONSE_LENGTH = 2000