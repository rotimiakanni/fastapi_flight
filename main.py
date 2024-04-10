from fastapi import FastAPI

from routers.customer import customer_router
from routers.flight import flight_router

app = FastAPI()

app.include_router(router=customer_router, prefix='/customers', tags=['customers'])
app.include_router(router=flight_router, prefix='/flights', tags=['flights'])

@app.get('/home')
def index():
    return "welcome onboard"