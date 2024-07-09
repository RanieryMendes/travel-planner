from sqlite3 import Connection
from typing import Dict, Tuple, List
class EmailsToInviteRepository:
    def __init__(self, conn:Connection) -> None:
        self.__conn=conn
    
    def register_email(self, email_info:Dict):
        cursor = self.__conn.cursor()  #get cursor from connection 
        cursor.execute(
            '''
                INSERT INTO emails_to_invite 
                    (id, trip_id, email) 
                VALUES 
                    (?, ?, ?)
            ''',
                (
                email_info["id"],
                email_info["trip_id"],
                email_info["email"],
                )
        )
        self.__conn.commit()

    def find_emails_from_trip (self, trip_id:str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM emails_to_invite WHERE trip_id = ?
            ''', 
                (trip_id,)
        ) # good practice to put a "," after the last item to be placed in the query
        trip = cursor.fetchall()
        
        return trip
    




