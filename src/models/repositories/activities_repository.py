from sqlite3 import Connection
from typing import Dict, Tuple, List
class ActivitiesRepository:
    def __init__(self, conn:Connection) -> None:
        self.__conn=conn
    
    def register_activity(self, activity_info:Dict):
        cursor = self.__conn.cursor()  #get cursor from connection 
        cursor.execute(
            '''
                INSERT INTO activities 
                    (id, trip_id, title, occurs_at) 
                VALUES 
                    (?, ?, ?, ?)
            ''',
                (
                activity_info["id"],
                activity_info["trip_id"],
                activity_info["title"],
                activity_info["occurs_at"],
                )
        )
        self.__conn.commit()

    def find_activities_from_trip (self, trip_id:str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM activities WHERE trip_id = ?
            ''', 
                (trip_id,)
        ) # good practice to put a "," after the last item to be placed in the query
        activities = cursor.fetchall()
       
        return activities

    




