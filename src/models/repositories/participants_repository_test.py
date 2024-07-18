import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .participants_repository import ParticipantsRepository

db_connection_handler.connect() #connect
trip_id = str(uuid.uuid4())
participant_id = str(uuid.uuid4())
# @pytest.mark.skip(reason="db integration")
def test_register_participants():
    conn = db_connection_handler.get_connection() #where we actually retrieve a connection session
    participants_repository = ParticipantsRepository(conn=conn)

    participants_info = {
        "id":participant_id,
        "trip_id":trip_id,
        "emails_to_invite_id":str(uuid.uuid4()),
        "name":"Raniery Mendes"
    }
        
    participants_repository.register_participants(participants_info=participants_info)

# @pytest.mark.skip(reason="db integration")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection() #where we actually retrieve a connection session
    participants_repository = ParticipantsRepository(conn=conn)

    participants = participants_repository.find_participants_from_trip(trip_id=trip_id)

    print()
    print(participants)

# @pytest.mark.skip(reason="db integration")
def test_update_participants_status():
    conn = db_connection_handler.get_connection() #where we actually retrieve a connection session
    participants_repository = ParticipantsRepository(conn=conn)

    participants_repository.update_participants_status(participant_id=participant_id)