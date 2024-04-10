from pydantic import BaseModel

class Customers(BaseModel):
    id: int
    name: str
    age: int
    phone: str

class CustomersCreate(BaseModel):
    name: str
    age: int
    phone: str


customers: dict[int, Customers] = {
    0: Customers(
        id=0, name='customer 0', age=30, phone='0800'
    ),
    1: Customers(
        id=1, name='customer 1', age=35, phone='0801'
    ),
    2: Customers(
        id=2, name='customer 2', age=20, phone='0802'
    )
}