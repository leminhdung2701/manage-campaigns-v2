from celery import Celery
import time

celery = Celery('tasks',broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')

# celery = Celery('tasks',broker='redis://default:redispw@localhost:55000',backend='redis://default:redispw@localhost:55000')


@celery.task
def calling(id_campaign,name_campaign,name_customer,phone):
    print("Calling "+ str(phone)+ " customer " + str(name_customer) + " in " + str(name_campaign)+" with id = "+str(id_campaign))
    time.sleep(2)
    return { 
            "name_customer":name_customer,
            "phone":phone,
            "status":"done"
            }