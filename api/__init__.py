""" Entry point """
import logging
from fastapi import FastAPI
from api.base.endpoints import index
from api.base.endpoints import average

logging.basicConfig(filename="app.log", level=logging.INFO)

app = FastAPI(
    title="Aire Logic Tech Test",
    description="Obtain average number of lyrics for an artist",
    version="0.0.1"
)

app.include_router(index.router)
app.include_router(average.router)
