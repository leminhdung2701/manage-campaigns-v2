from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    phone_number: str
    any: str
    
    