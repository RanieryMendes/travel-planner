from flask import jsonify, Blueprint, request
from src.controllers.trip_creator import TripCreator #import controller
#import repos
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
#import db manager
from src.models.settings.db_connection_handler import db_connection_handler

trip_routes_bp = Blueprint("trip_routes", __name__)

@trip_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository =  TripsRepository(conn=conn)
    emails_repository = EmailsToInviteRepository(conn=conn)
    controller =  TripCreator(trip_repository=trips_repository, emails_repository=emails_repository)
    
    response = controller.create(request.json)
    
    return jsonify(response["body"]), response["status_code"]