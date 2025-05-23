from openai import OpenAI
from tenacity import retry, wait_random_exponential, stop_after_attempt


class OpenAIClient:
    def __init__(
        self,
        api_key: str,
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.5,
        max_tokens: int = 100,
    ):
        self.client = OpenAI(api_key=api_key)  # New client instance
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def chat(self, prompt: str, max_tokens: int = None) -> str:
        """Make a GPT chat completion call with retry logic and token control."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=max_tokens or self.max_tokens,
        )
        return response.choices[0].message.content.strip()
