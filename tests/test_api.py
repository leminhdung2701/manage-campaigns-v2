from fastapi.testclient import TestClient 
from server.api.database.db import collection_campaign,collection_status_campaign
from main import app 


client = TestClient(app)

data = {
  "name": "Ban hang Laptop sinh vien",
  "customer_data": [
    {
      "name": "Dung",
      "phone_number": "0945153685",
      "any": "MAC"
    },
     {
      "name": "Duy",
      "phone_number": "0943434434",
      "any": "Dell"
    },
     {
      "name": "Hung",
      "phone_number": "0965432224",
      "any": "HP"
    },
     {
      "name": "Lan",
      "phone_number": "0765433556",
      "any": "Acer"
    },
     {
      "name": "Giang",
      "phone_number": "0856743556",
      "any": "Lenovo"
    }
  ]
}

def test_create_campaingn():
    response = client.post("/campaign/create/", json=data)
    assert response.status_code == 200

def test_update_campaingn():
    campaign = list(collection_campaign.find())[0]
    id = campaign["_id"]
    response = client.put("/campaign/"+str(id)+"/update/", json = {
        "name": "Ban hang Laptop sinh vien",
        "customer_data": [
            {
            "name": "Dung",
            "phone_number": "0945153685",
            "any": "MAC"
            },
            {
            "name": "Duy",
            "phone_number": "0943434434",
            "any": "Dell"
            },
            {
            "name": "Hung",
            "phone_number": "0965432224",
            "any": "HP"
            }]
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": str(id),
        "name": "Ban hang Laptop sinh vien",
        "customer_data": [
            {
            "name": "Dung",
            "phone_number": "0945153685",
            "any": "MAC"
            },
            {
            "name": "Duy",
            "phone_number": "0943434434",
            "any": "Dell"
            },
            {
            "name": "Hung",
            "phone_number": "0965432224",
            "any": "HP"
            }]
    }

    
def test_start_campaingn():
    campaign = list(collection_campaign.find())[0]
    id = campaign["_id"]
    response = client.put("/campaign/"+str(id)+"/start/")
    assert response.status_code == 200
   
    
def test_stop_campaingn():
    campaign = list(collection_status_campaign.find())[0]
    id = campaign["id_campaign"]
    response = client.put("/campaign/"+str(id)+"/stop/")
    assert response.status_code == 200
    

def test_duplicate_campaingn():
    campaign = list(collection_campaign.find())[0]
    id = campaign["_id"]
    response = client.put("/campaign/"+str(id)+"/duplicate/")
    assert response.status_code == 200
    
def test_disable_campaingn():
    campaign = list(collection_status_campaign.find())[0]
    id = campaign["id_campaign"]
    response = client.put("/campaign/"+str(id)+"/disable/")
    assert response.status_code == 200
    
 