from typing import List
from pydantic import BaseModel
from server.api.database.models.customer import Customer
 
class Campaign(BaseModel):
    name: str   
    customer_data: List[Customer]
    

    
    
    
    