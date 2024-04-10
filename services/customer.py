from schema.customer import customers, Customers, CustomersCreate

class CustomerSerivce:

    @staticmethod
    def parse_customers(customer_data):
        data = []
        for cust in customer_data:
            data.append(customers[cust])
        return data
    
    @staticmethod
    def get_customer_by_id(customer_id):
        return customers[customer_id]
    
    @staticmethod
    def create_customer(customer_data: CustomersCreate):
        id = len(customers)
        customer = Customers(
            id=id,
            **customer_data.model_dump()
        )
        customers[id] = customer
        return customer