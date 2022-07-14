
def serializer_status_campaign(campaign) -> dict:
    return {
        "id_campaign": campaign["id_campaign"],
        "status": campaign["status"],
        "active": campaign["active"],
    }



def serializer_status_campaigns(campaigns) -> list:
    return [serializer_status_campaign(campaign) for campaign in campaigns]