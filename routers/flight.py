from fastapi import APIRouter

from schema.flight import FlightsCreate
from services.flight import FlightService

flight_router = APIRouter()

@flight_router.post('', status_code=201)
def create_flight(payload: FlightsCreate):
    data = FlightService.create_flight(payload)
    return data