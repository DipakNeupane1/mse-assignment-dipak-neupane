#Week 7 - Activity 1 (part1) : Design Pattern - Tips for Python exercises
#Develop a code, record the processing time, 
# and share the results. Provide the GitHub link for reference. Hint: You may adjust the queries to align with your database structure. - See below file
import sqlite3
from datetime import datetime
class BookService:
   def  get_book(self, book_id):
       print(f"Get book =======>>")
       print(f"Requested on :: {datetime.now()}")
       db_conn = sqlite3.connect('library.db')
       cursor = db_conn.cursor()
       cursor.execute('Select * from books where id = ?',(book_id,))
       row = cursor.fetchone()
       if not row:
           print(" Row not found ::")
       cursor.close()
       print(f"Requested finished on :: {datetime.now()}")
       return row
   
   def get_books(self):
        print(f"Get books =======")
        print(f"Requested time is :: {datetime.now()}")
        db_conn = sqlite3.connect('library.db')
        cursor = db_conn.cursor()
        cursor.execute('Select * from books where 1=1')
        row = cursor.fetchone()
        print(f"Row size is :: {len(row)}")
        cursor.close()
        print(f"Requested finished on :: {datetime.now()}")
        return row
    
if __name__ == "__main__":
    book_service = BookService()
    book_service.get_book(1)
    book_service.get_books()
        
        
        