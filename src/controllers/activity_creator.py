import uuid
from typing import Dict

class ActivityCreator:
    def __init__(self, activity_repository) -> None:
        self.__activity_repository = activity_repository

    def create (self, body, trip_id) -> None:
        try:
            id = str(uuid.uuid4())
            activities_info ={
                "id":id,
                "trip_id":trip_id,
                "title":body["title"],
                "occurs_at":body["occurs_at"]
            }

            self.__activity_repository.register_activity(activities_info)

            return {
                "body":{"activityId": id},
                "status_code":201
            }

        except Exception as exception:
            return {
                "body":{"error":"Bad Request", "message": str(exception)},
                "status_code": 400
            }