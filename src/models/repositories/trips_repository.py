from sqlite3 import Connection
from typing import Dict, Tuple
class TripsRepository:
    def __init__(self, conn:Connection) -> None:
        self.__conn=conn
    
    def create_trip(self, trips_info:Dict):
        cursor = self.__conn.cursor()  #get cursor from connection 
        cursor.execute(
            '''
                INSERT INTO trips 
                    (id, destination, start_date, end_date, owner_name, owner_email) 
                VALUES 
                    (?, ?, ?, ?, ?, ?)
            ''',(
                trips_info["id"],
                trips_info["destination"],
                trips_info["start_date"],
                trips_info["end_date"],
                trips_info["owner_name"],
                trips_info["owner_email"]
            )
        )
        self.__conn.commit()

    def find_trip_by_id(self, trip_id:str) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM trips WHERE id = ?
            ''', (trip_id,)
        ) # good practice to put a "," after the last item to be placed in the query
        trip = cursor.fetchone()
        
        return trip


