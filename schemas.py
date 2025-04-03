from pydantic import BaseModel

class DataIn(BaseModel):
    data: str | None = None
