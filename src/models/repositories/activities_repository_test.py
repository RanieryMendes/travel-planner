import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .activities_repository import ActivitiesRepository


db_connection_handler.connect() #connect
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="db integration")
def test_register_activity():
    conn = db_connection_handler.get_connection() #where we actually retrieve a connection session
    activities_repository = ActivitiesRepository(conn=conn)

    actvities_infos = {
        "id":str(uuid.uuid4()),
        "trip_id":trip_id,
        "title":"Signing job contract",
        "occurs_at":"07-22-2024"
    }

    activities_repository.register_activity(activity_info=actvities_infos)



@pytest.mark.skip(reason="db integration")
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection() #where we actually retrieve a connection session
    activities_repository = ActivitiesRepository(conn=conn)

    activities = activities_repository.find_activities_from_trip(trip_id=trip_id)
    print()
    print(activities)