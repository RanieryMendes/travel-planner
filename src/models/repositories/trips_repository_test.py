import pytest 
import uuid
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler
from datetime import datetime, timedelta

db_connection_handler.connect()

trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="db integration")
def test_create_trip():
    conn= db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn=conn)

    trips_infos = {
        "id":trip_id,
        "destination":"Maldives",
        "start_date": datetime.strptime("12-23-2024", "%m-%d-%Y"),
        "end_date": datetime.strptime("12-23-2024", "%m-%d-%Y") + timedelta(days=5),
        "owner_name":"Raniery Mendes",
        "owner_email":"ranierymendes@outlook.com"
    }

    trips_repository.create_trip(trips_info=trips_infos)

@pytest.mark.skip(reason="db integration")
def test_find_trip_by_id(): #find element
    conn= db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn=conn)

    trip = trips_repository.find_trip_by_id(trip_id=trip_id)

@pytest.mark.skip(reason="db integration")
def test_update_trip_status():
    conn= db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn=conn)

    trip = trips_repository.update_trip_status(trip_id=trip_id)
  

