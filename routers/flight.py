from fastapi import APIRouter

from schema.flight import FlightsCreate, flights
from services.flight import FlightService

flight_router = APIRouter()

@flight_router.post('', status_code=201)
def create_flight(payload: FlightsCreate):
    data = FlightService.create_flight(payload)
    return {'message': 'success', 'data': data}

@flight_router.get('', status_code=200)
def get_flights():
    return {'message': 'success', 'data': flights}

@flight_router.get('/{flight_id}')
def get_flight_by_id(flight_id: int):
    data = FlightService.get_flight_by_id(flight_id)
    return {'message': 'success',  'data': data}

@flight_router.put('/{flight_id}')
def edit_flight(flight_id: int, payload: FlightsCreate):
    data = FlightService.edit_flight(flight_id, payload)
    return {'message': 'success', 'data': data}

@flight_router.delete('/{flight_id}', status_code=200)
def delete_flight(flight_id: int):
    FlightService.delete_flight(flight_id)
    return {'Flight deleted successfully.'}