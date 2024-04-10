from schema.flight import FlightsCreate, flights, Flights
from schema.customer import customers

class FlightService:

    @staticmethod
    def create_flight(payload: FlightsCreate):
        id = len(flights)
        customer = customers[payload.customer]
        flight = Flights(
            id=id,
            customer=customer,
            destination=payload.destination,
            origin=payload.origin,
            duration=payload.duration,
            price=payload.price
        )
        flights.append(flight)
        return flight