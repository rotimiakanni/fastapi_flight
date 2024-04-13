from schema.flight import flights

class FlightHelpers:

    @staticmethod
    def get_flight_by_id(flight_id: int):
        for flight in flights:
            if flight.id == flight_id:
                return flight
        return None