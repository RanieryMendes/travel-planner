from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler
import pytest
import uuid

db_connection_handler.connect()

link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="db integration")
def test_register_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn=conn)

    link_info = {
        "id":link_id,
        "trip_id":trip_id,
        "link":"test.com",
        "title": "The Trip"
    }

    link_repository.register_link(link_info=link_info)

@pytest.mark.skip(reason="db integration")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn=conn)

    response = link_repository.find_links_from_trip(trip_id=trip_id)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)