from server.api.database.db import collection_status_campaign, collection_campaign, collection_customers
from fastapi.encoders import jsonable_encoder
from server.api.database.models.status_campaign import StatusCampaign
from server.api.schema.status_campaign import serializer_status_campaign
from bson import ObjectId



def update_true_status_campaign(id):
    status_campaign = StatusCampaign(id_campaign=id,status=True,active=True)
    if len(list(collection_status_campaign.find({"id_campaign":id}))) == 0: 
        collection_status_campaign.insert_one(jsonable_encoder(status_campaign))
        insert_customer(id)
    else: 
        list_status_campaign = list(collection_status_campaign.find({"id_campaign":id}))
        active_campaign = list_status_campaign[0]["active"]
        if active_campaign:
            collection_status_campaign.find_one_and_update({"id_campaign":id},{
                "$set":jsonable_encoder(status_campaign)
            })
        else:
            return {"This campaign is disabled"}
    return serializer_status_campaign(collection_status_campaign.find_one({"id_campaign":id}))

def update_false_status_campaign(id):
    status_campaign = StatusCampaign(id_campaign=id,status= False)
    
    if len(list(collection_status_campaign.find({"id_campaign":id}))) == 0: 
        return {"This campaign hasn't started"}
    else: 
        list_status_campaign = list(collection_status_campaign.find({"id_campaign":id}))
        active_campaign = list_status_campaign[0]["active"]
        if active_campaign:
            collection_status_campaign.find_one_and_update({"id_campaign":id},{
                "$set":jsonable_encoder(status_campaign)
            })
        else:
            return {"This campaign is disabled"}
    return serializer_status_campaign(collection_status_campaign.find_one({"id_campaign":id}))

def update_false_disable_campaign(id):
    if len(list(collection_status_campaign.find({"id_campaign":id}))) == 0: 
        return {"This campaign hasn't started"}
    else: 
        list_status_campaign = list(collection_status_campaign.find({"id_campaign":id}))
        active_campaign = list_status_campaign[0]["active"]
        status_campaign = list_status_campaign[0]["status"]
        if active_campaign:
            status_campaign = StatusCampaign(id_campaign=id,status =status_campaign ,active= False)
            collection_status_campaign.find_one_and_update({"id_campaign":id},{
                "$set":jsonable_encoder(status_campaign)
            })
        else:
            return {"This campaign is disabled"}
    return serializer_status_campaign(collection_status_campaign.find_one({"id_campaign":id}))

def insert_customer(id):
    campaigns = get_campaign(id)
    if len(campaigns) > 0:
        campaign = campaigns[0]
        customers = list(campaign["customer_data"])
        for customer in customers:
            cont = {
                "id_campaign":str(campaign["_id"]),
                "name_campaign":campaign["name"],
                "name_customer":customer["name"],
                "phone":customer["phone_number"],
                "status":True
            }
            collection_customers.insert_one(cont)
            
    
def get_campaign(id):
    a = list(collection_campaign.find({"_id":ObjectId(id)}))
    if len(a) > 0: return a
    else: return []
    
    
def check_status_customer(id_customer):
    list_customers = list(collection_customers.find({"_id":ObjectId(id_customer)}))
    status_customer = list_customers[0]["status"]
    id_campaign = list_customers[0]["id_campaign"]
    list_status_campaign = list(collection_status_campaign.find({"id_campaign":id_campaign}))
    active_campaign = list_status_campaign[0]["active"]
    status_campaign = list_status_campaign[0]["status"]
    # print(active_campaign,status_campaign,status_customer)
    if active_campaign and status_campaign and status_customer: 
        return True
    else: 
        return False
    
def get_customers():
    return list(collection_customers.find({"status":True}))

def update_status_customer(id):
    collection_customers.find_one_and_update({"_id":ObjectId(id)},{
        "$set":{
            "status":False
        }
    })
    