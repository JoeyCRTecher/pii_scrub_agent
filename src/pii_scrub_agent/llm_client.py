"""LLM client for communicating with language models."""

import json
import requests
from typing import Dict, Any, Optional


class LLMClient:
    """Client for communicating with language model APIs."""
    
    def __init__(self, base_url: str):
        """Initialize the LLM client.
        
        Args:
            base_url: Base URL for the LLM API endpoint
        """
        self.base_url = base_url.rstrip('/')
    
    def prompt(self, message: str, model_name: str) -> str:
        """Send a prompt to the LLM and return the response.
        
        Args:
            message: The prompt message to send
            model_name: Name of the model to use
            
        Returns:
            The response from the LLM
            
        Raises:
            requests.RequestException: If the API request fails
        """
        # Standard OpenAI-compatible API format
        payload = {
            "model": model_name,
            "messages": [
                {"role": "user", "content": message}
            ],
            "temperature": 0.1,
            "max_tokens": 1000
        }
        
        headers = {
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            f"{self.base_url}/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        response.raise_for_status()
        result = response.json()
        
        return result["choices"][0]["message"]["content"]