from pydantic import BaseModel
from decimal import Decimal

from schema.customer import Customers, customers

class Flights(BaseModel):
    id: int
    customer: Customers
    origin: str
    destination: str
    duration: str
    price: Decimal

class FlightsCreate(BaseModel):
    customer: int
    origin: str
    destination: str
    duration: str
    price: Decimal


flights: list[Flights] = [
    Flights(
        id=0, customer=customers[0], origin='Lagos', destination='Abuja',
        duration='1 hour', price=Decimal('100000')
    )
]