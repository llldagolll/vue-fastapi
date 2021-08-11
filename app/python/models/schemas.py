from typing import List
from pydantic import BaseModel

# モデル定義(apiのモデル) 
class TestTaskBase(BaseModel):
    name: str
    content: str


class TestTaskCreate(TestTaskBase):
    pass 


class Task(TestTaskBase):
    name: str
    content: str

    class Config:
        orm_mode = True