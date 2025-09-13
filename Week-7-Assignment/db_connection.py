#Week7 Activity1- part2: design pattern
#Compare the coding outcomes and processing time when using the Singleton design pattern in OOP (Week 7 – Activity 1) 
# within your coding style. Share the GitHub link and add a short comment explaining it.
 
import sqlite3

class DatabaseConnection:
     _instance = None
     _connection = None

     def __new__(self):
        if self._instance is None:
            self._instance = super(DatabaseConnection, self).__new__(self)
            self._connection = sqlite3.connect("library.db", check_same_thread=False)
        return self._instance

     def get_connection(self):
         return self._connection