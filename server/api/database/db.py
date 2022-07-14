from pymongo import MongoClient

url_campaign = f'mongodb+srv://minhdung:H7AXRCqUFA3xWfGi@CampaignDB.591j1.mongodb.net/?retryWrites=true&w=majority'
url_schedule = f'mongodb+srv://minhdung:K2cQ0buUPfC1eweP@scheduledb.8tsbu.mongodb.net/?retryWrites=true&w=majority'


client_campaign = MongoClient(url_campaign)
client_schedule = MongoClient(url_schedule)


db_campaign = client_campaign.database 
db_schedule = client_schedule.database

collection_campaign = db_campaign["campaign"]

collection_status_campaign = db_schedule["status_campaign"]

collection_customers = db_schedule["customers"]
