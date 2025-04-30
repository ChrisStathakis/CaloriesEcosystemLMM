import requests
import json
import time
import os
from typing import List, Dict, Any, Optional


class OllamaAgent:

    def __init__(self,
                 model_name: str = "llama3",
                 temperature: float = 0.7,
                 max_tokens: int = 1000,
                 base_url: str = "http://localhost:11434"
                 ):
        """
               Initialize the Ollama-based AI agent.

               Args:
                   model_name: The name of the Ollama model to use
                   temperature: Controls randomness in responses (0.0 to 1.0)
                   max_tokens: Maximum number of tokens in generated responses
                   base_url: The URL where Ollama API is hosted
        """

        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.base_url = base_url
        self.conversation_history = []
        self.api_endpoint = f"{base_url}/api/generate"

        self._check_ollama_server()

    def _check_ollama_server(self) -> None:

        try:
            response = requests.get(f'{self.base_url}/api/tags')
            if response.status_code != 200:
                raise ConnectionError(f'Ollama server not responding correctly: {response.status_code}')

            available_models = response.json().get("models", [])
            model_names = [model.get("name") for model in available_models]

            if self.model_name not in model_names:
                print(f"Warning: Model '{self.model_name}' not found. Available models: {model_names}")
                print(f"You may need to run: 'ollama pull {self.model_name}'")

        except:
            raise ConnectionError("Cannot connect to Ollama server. Is it running on localhost:11434?")

    def add_to_history(self, role: str, content: str) -> None:
        self.conversation_history.append(({"role": role, "content": content}))

    def format_prompt(self) -> str:
        formatted_prompt = ""

        for message in self.conversation_history:
            if message["role"] == "user":
                formatted_prompt += f"User: {message['content']}\n"
            else:
                formatted_prompt += f"Assistant: {message['content']}\n"
        formatted_prompt += f'Assistant: '
        return formatted_prompt

    def generate_response(self, user_query: str) -> str:
        self.add_to_history("user", user_query)
        prompt = self.format_prompt()

        payload = {
            "model": self.model_name
        }
