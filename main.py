import uvicorn
from fastapi import FastAPI
from server.api.routers.campaign import router_campaign
from server.config import LOGGING
import uvicorn
import logging.config

app = FastAPI()

app.include_router(router_campaign)

if __name__ == '__main__':
    logging.config.dictConfig(LOGGING)
    uvicorn.run(app, host='127.0.0.1', port=8000)