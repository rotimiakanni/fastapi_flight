from fastapi import HTTPException

from schema.flight import FlightsCreate, Flights, flights
from schema.customer import Customers, customers
from utils.flight import FlightHelpers

class FlightService:

    @staticmethod
    def create_flight(payload: FlightsCreate):
        id = len(flights)
        customer: Customers = customers[payload.customer]
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
    
    @staticmethod
    def get_flight_by_id(flight_id: int):
        flight = FlightHelpers.get_flight_by_id(flight_id)
        if not flight:
            raise HTTPException(detail='Flight not found', status_code=404)
        return flight
    
    @staticmethod
    def edit_flight(flight_id: int, payload: FlightsCreate):
        flight: Flights  = FlightHelpers.get_flight_by_id(flight_id)
        if not flight:
            raise HTTPException(detail='Flight not found', status_code=404)
        customer: Customers = customers[payload.customer]

        flight.origin = payload.origin
        flight.destination = payload.destination
        flight.duration = payload.duration
        flight.price = payload.price
        flight.customer = customer
        return flight
    
    @staticmethod
    def delete_flight(flight_id):
        flight: Flights  = FlightHelpers.get_flight_by_id(flight_id)
        if not flight:
            raise HTTPException(detail='Flight not found', status_code=404)
        del flights[flight_id]