from flask import jsonify, Blueprint, request
#import controllers 
from src.controllers.trip_creator import TripCreator 
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmation import TripConfirmation

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_confirmation import ParticipantConfirmation
from src.controllers.participant_finder import ParticipantFinder

from src.controllers.activity_finder import ActivityFinder
from src.controllers.activity_creator import ActivityCreator

#import repos
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.participants_repository import ParticipantsRepository

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

@trip_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn=conn)
    
    controller = LinkCreator(link_repository=links_repository)
    response = controller.create(request.json, trip_id=tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn=conn)
    
    controller = LinkFinder(link_repository=links_repository)
    response = controller.find(tripId=tripId)

    return jsonify(response["body"]), response["status_code"]



@trip_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn=conn)
    emails_repository = EmailsToInviteRepository(conn=conn)

    controller = ParticipantCreator(participants_repository=participants_repository, emails_repository=emails_repository)
    response = controller.create(request.json, trip_id=tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn=conn)
    
    controller = ActivityCreator(activity_repository=activities_repository)
    response = controller.create(request.json, trip_id =tripId)

    return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn=conn)

    controller = ParticipantFinder(participants_repository=participants_repository)
    response = controller.find_participants_from_trip(trip_id=tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn=conn)

    controller = ActivityFinder(activities_repository=activities_repository)
    response = controller.find_from_trip(trip_id=tripId)

    return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn=conn)

    controller = ParticipantConfirmation(participants_repository=participants_repository)
    response = controller.confirm(participantId)

    return jsonify(response["body"]), response["status_code"]
