# ai_ad_generation.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

class AIGeneration:
    @staticmethod
    def generate_ad(prompt, max_tokens=60):
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()