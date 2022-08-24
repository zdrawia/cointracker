from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    username: str
    balance: float
    
    class Config:
        orm_mode = True