from fastapi import APIRouter, Response

from schema.customer import customers, CustomersCreate
from services.customer import CustomerSerivce

customer_router = APIRouter()

@customer_router.get('/', status_code=200)
def get_customers():
    data = CustomerSerivce.parse_customers(customer_data=customers)
    return {'message': 'successful', 'data': data}

@customer_router.get('/{customer_id}', status_code=200)
def get_customer_by_id(customer_id: int):
    data =  CustomerSerivce.get_customer_by_id(customer_id)
    return {'message': 'successful', 'data': data} 

@customer_router.post('/', status_code=201)
def create_customer(payload: CustomersCreate):
    data = CustomerSerivce.create_customer(payload)
    return {'message': 'Created', 'data': data}