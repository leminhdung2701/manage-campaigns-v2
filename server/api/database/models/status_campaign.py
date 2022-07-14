from pydantic import BaseModel

class StatusCampaign(BaseModel):
    id_campaign: str
    status: bool = True
    active: bool = True
    