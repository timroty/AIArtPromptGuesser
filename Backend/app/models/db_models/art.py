from datetime import datetime
from typing import Optional
import json

class Art:
    def __init__(self, id, created_at, reference_url, prompt, model):
        self.id: int = id
        self.created_at: datetime = created_at
        self.reference_url: Optional[str] = reference_url
        self.prompt: Optional[str] = prompt
        self.model: Optional[str] = model

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get('id'),
            created_at=data.get('created_at'),
            reference_url=data.get('reference_url'),
            prompt=data.get('prompt'),
            model=data.get('model'),
        )
    
    def jsonify(self):
        return json.dumps({
            "id": self.id,
            "reference_url": self.reference_url,
            "prompt": self.prompt,
            "model": self.model
        })