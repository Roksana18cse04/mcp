from typing import Union
import json

class ToolCallRequest:
    def __init__(self, body: Union[str, dict]):
        self.body = body

    def text(self) -> str:
        if isinstance(self.body, dict) and "text" in self.body:
            return self.body["text"]
        elif isinstance(self.body, str):
            return self.body
        raise ValueError("No text content found.")

    def json(self) -> dict:
        if isinstance(self.body, dict):
            return self.body
        elif isinstance(self.body, str):
            try:
                return json.loads(self.body)
            except json.JSONDecodeError:
                raise ValueError("Payload string is not valid JSON.")
        raise ValueError("Payload is not JSON-serializable.")
