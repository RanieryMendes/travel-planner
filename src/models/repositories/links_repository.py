from sqlite3 import Connection
from typing import Dict, Tuple, List

class LinksRepository:
    def __init__(self, conn:Connection) -> None:
        self.__conn=conn
    
    def register_link(self, link_info:Dict):
        cursor = self.__conn.cursor()  #get cursor from connection 
        cursor.execute(
            '''
                INSERT INTO links 
                    (id, trip_id, link, title) 
                VALUES 
                    (?, ?, ?, ?)
            ''',
                (
                link_info["id"],
                link_info["trip_id"],
                link_info["link"],
                link_info["title"]
                )
        )
        self.__conn.commit()

    def find_links_from_trip (self, trip_id:str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM links WHERE trip_id = ?
            ''', 
                (trip_id,)
        ) # good practice to put a "," after the last item to be placed in the query
        links = cursor.fetchall()
        
        return links
    




