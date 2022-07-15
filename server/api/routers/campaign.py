from bson import ObjectId
from fastapi import APIRouter
from server.api.database.models.campaign import Campaign
from server.api.database.db import collection_campaign
from server.api.schema.campaign import serializer_campaign
from fastapi.encoders import jsonable_encoder
from server.api.scheduler.process_db import update_true_status_campaign,update_false_status_campaign, update_false_disable_campaign

router_campaign = APIRouter() 

@router_campaign.post('/campaign/create/')
async def create_campaign(campaign: Campaign):
    _id = collection_campaign.insert_one(jsonable_encoder(campaign))
    return serializer_campaign(collection_campaign.find_one({"_id": _id.inserted_id}))

@router_campaign.put('/campaign/{id}/update/')
async def update_campaign(id: str,campaign: Campaign):
    collection_campaign.find_one_and_update({"_id":ObjectId(id)},{
        "$set":jsonable_encoder(campaign)
    })
    return serializer_campaign(collection_campaign.find_one({"_id":ObjectId(id)}))

@router_campaign.put('/campaign/{id}/start/')
async def start_campaign(id: str):
    if len(list(collection_campaign.find({"_id":ObjectId(id)}))) > 0:
        return update_true_status_campaign(id)
    else:
        return {"Not Found ID"}

@router_campaign.put('/campaign/{id}/stop/')
async def stop_campaign(id: str):
    if len(list(collection_campaign.find({"_id":ObjectId(id)}))) > 0:
        return update_false_status_campaign(id)
    else:
        return {"Not Found ID"}

@router_campaign.put('/campaign/{id}/disable/')
async def disable_campaign(id: str):
    return update_false_disable_campaign(id)
   
@router_campaign.put('/campaign/{id}/duplicate/')        
async def duplicate_campaign(id):
    list_campaign = list(collection_campaign.find({"_id":ObjectId(id)}))
    
    if len(list_campaign) == 0: 
        return {"This campaign doesn't exist"}
    else:
        campaign = Campaign(name = list_campaign[0]["name"],customer_data = list_campaign[0]["customer_data"])
        _id = collection_campaign.insert_one(jsonable_encoder(campaign))
        return serializer_campaign(collection_campaign.find_one({"_id": _id.inserted_id}))  


    
    

    
