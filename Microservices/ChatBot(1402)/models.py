from pydantic import BaseModel


class ChatGPTMessage(BaseModel):
    model: str
    prompt: str
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float