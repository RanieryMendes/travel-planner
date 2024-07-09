import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect() #connect
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="db integration")
def test_register_email():
    conn = db_connection_handler.get_connection() #where we actually retrieve a connection session
    emails_to_invite_repository = EmailsToInviteRepository(conn=conn)

    emails_trips_infos = {
        "id":str(uuid.uuid4()),
        "trip_id":trip_id,
        "email":"mendrc18@wfu.edu"
    }

    emails_to_invite_repository.register_email(email_info=emails_trips_infos)

@pytest.mark.skip(reason="db integration")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection() #where we actually retrieve a connection session
    emails_to_invite_repository = EmailsToInviteRepository(conn=conn)

    emails = emails_to_invite_repository.find_emails_from_trip(trip_id=trip_id)
    print()
    print(emails)