from flask import jsonify, Blueprint, request
from src.controllers.trip_creator import TripCreator #import controller
from src.controllers.trip_finder import TripFinder
from src.controllers.link_creator import LinkCreator
from src.controllers.trip_confirmation import TripConfirmation
#import repos
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
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

@trip_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository =  TripsRepository(conn=conn)
    controller = TripFinder(trips_repository=trips_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository =  TripsRepository(conn=conn)
    controller = TripConfirmation(trips_repository=trips_repository)

    response = controller.confirm(tripId)  

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/confirm", methods=["POST"])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn=conn)
    controller = LinkCreator(link_repository=links_repository)

    response = controller.create(request.json, trip_id=tripId)

    return jsonify(response["body"]), response["status_code"]
