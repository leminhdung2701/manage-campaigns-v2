from celery import Celery
import asyncio

celery = Celery('tasks',broker='redis://redis:6379/0',backend='redis://redis:6379/0')

@celery.task
def calling(id_campaign,name_campaign,name_customer,phone):
    print("Calling "+ str(phone)+ " customer " + str(name_customer) + " in " + str(name_campaign)+" with id = "+str(id_campaign))
    asyncio.sleep(20)
    return { 
            "name_customer":name_customer,
            "phone":phone,
            "status":"done"
            }