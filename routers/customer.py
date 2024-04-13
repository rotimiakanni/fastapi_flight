from fastapi import APIRouter, Response

from schema.customer import customers, CustomersCreateEdit
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
def create_customer(payload: CustomersCreateEdit):
    data = CustomerSerivce.create_customer(payload)
    return {'message': 'Created', 'data': data}

@customer_router.put('/{customer_id}', status_code=200)
def edit_customer(customer_id: int, payload: CustomersCreateEdit):
    data = CustomerSerivce.edit_customer(payload)
    return {'message': 'success', 'data': data}

@customer_router.delete('/{customer_id}')
def delete_customer(customer_id: int):
    CustomerSerivce.delete_customer(customer_id)
    return {'messge': 'user deleted successfully.'}