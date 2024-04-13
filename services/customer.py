from fastapi import HTTPException
from schema.customer import customers, Customers, CustomersCreateEdit

class CustomerSerivce:

    @staticmethod
    def parse_customers(customer_data):
        data = []
        for cust in customer_data:
            data.append(customers[cust])
        return data
    
    @staticmethod
    def get_customer_by_id(customer_id):
        customer = customers.get(customer_id)
        if not customer:
            raise HTTPException(detail='Customer not found.', status_code=404)
        return customer
    
    @staticmethod
    def create_customer(customer_data: CustomersCreateEdit):
        id = len(customers)
        customer = Customers(
            id=id,
            **customer_data.model_dump()
        )
        customers[id] = customer
        return customer
    
    @staticmethod
    def edit_customer(payload: CustomersCreateEdit):
        id = len(customers)
        customer = Customers(
            id=id,
            **payload.model_dump()
        )
        customers[id] = customer
        return customer
    
    @staticmethod
    def delete_customer(customer_id: int):
        customer = customers.get(customer_id)
        if not customer:
            raise HTTPException(detail='Customer not found.', status_code=404)
        del customers[customer_id]
