
def serializer_campaign(campaign) -> dict:
    return {
        "id": str(campaign["_id"]),
        "name": campaign["name"],
        "customer_data": campaign["customer_data"]
    }



def serializer_campaigns(campaigns) -> list:
    return [serializer_campaign(campaign) for campaign in campaigns]