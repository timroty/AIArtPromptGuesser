from datetime import datetime
from typing import Optional

class Art:
    def __init__(self, id, created_at, reference_url, prompt):
        self.id: int = id
        self.created_at: datetime = created_at
        self.reference_url: Optional[str] = reference_url
        self.prompt: Optional[str] = prompt

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get('id'),
            created_at=data.get('created_at'),
            reference_url=data.get('reference_url'),
            prompt=data.get('prompt'),
        )