from celery_worker import calling,sync_task
from server.api.scheduler.process_db import check_status_customer,get_customers, update_status_customer

def run():
        print("I'm checking the database for campaigns to run.")
        count = 0
        while True:
            all_customers = get_customers()
            if len(all_customers[count:]) >0:
                if len(all_customers[count:]) >= 8: 
                    customers = all_customers[count:count+8]
                    count = count + 8
                else:  
                    customers = all_customers[count:]
                    count = count + len(all_customers[count:])
                for customer in customers:
                    id_customer = str(customer["_id"])
                    if check_status_customer(id_customer):
                        id_campaign = customer["id_campaign"]
                        name_campaign = customer["name_campaign"]
                        name_customer = customer["name_customer"]
                        phone = customer["phone"]
                        print("................................................................")
                        print("ID: "+str(id_customer)+" - Calling "+ str(phone)+ " customer " + str(name_customer) + " in " + str(name_campaign)+" with id = "+str(id_campaign))
                        sync_task.delay(id_campaign,name_campaign,name_customer,phone)
                        update_status_customer(str(customer["_id"]))
            else:
                print("----------------------------------------------------------------")
                print("Wait tasks...")
                count = 0
                
       