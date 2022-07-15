from celery import Celery
import asyncio, time
from asgiref.sync import async_to_sync


celery = Celery('tasks',broker='redis://redis:6379/0',backend='redis://redis:6379/0')

async def calling(id_campaign,name_campaign,name_customer,phone):
    print("Calling "+ str(phone)+ " customer " + str(name_customer) + " in " + str(name_campaign)+" with id = "+str(id_campaign))
    await asyncio.sleep(20)
    return { 
            "name_customer":name_customer,
            "phone":phone,
            "status":"done"
            }

@celery.task(name="sync_task")
def sync_task(id_campaign,name_campaign,name_customer,phone):
    async_to_sync(calling)(id_campaign,name_campaign,name_customer,phone)
    