import pymysql

# The commands which operate on the MySQL database
db_command = {
    "Create" : 'CREATE TABLE IF NOT EXISTS %s (Name text, Icon text, Start text, Frequency text, Reminder text)', # Create a table storing a user and his habits
    "Insert" : "INSERT INTO %s (Name, Icon, Start, Frequency, Reminder)VALUES('%s', '%s', '%s', '%s', '%s')",     # Insert a habit 
    "Read"   : "SELECT * FROM %s",                                                                                # Read all habits of a user 
    "Select" : "SELECT * FROM %s WHERE Name = %s",                                                                # Read the specific habit 
    "Update" : "UPDATE %s SET Icon = '%s', Start = '%s', Frequency = '%s', Reminder = '%s' WHERE Name = '%s'",    # Update the information of a habit
    "Delete" : "DELETE FROM %s WHERE Name = '%s'"                                                                 # Delete a habit 
}

class MySQL:
    # Connect local MySQL database 
    # @host : ip address
    # @port : user's name
    # @user : MySQL account
    # @password : MySQL password
    # @db : name of database
    # @charset : character set 
    # @return : None
    def __init__(self, host='localhost', port=3306, user='root', password="", db='habit_tracker', charset='utf8') :
        self.db_settings = {"host": host, "port": port, "user": user, "password": password,"db": db,"charset": charset}
        self.connect_db = pymysql.connect(**self.db_settings)
    
    # Create a table named by username and storing his habits
    # @username : user's name
    # @return : None
    def createUser(self, username):
        with self.connect_db.cursor() as cursor:
            cursor.execute(db_command["Create"]%username)
            self.connect_db.commit()
    
    # Insert a new habit
    # @username : user's name
    # @newHabit :  habit to be inserted
    # @return : List of Habit which are user's habits
    def insertHabit(self, username, newhabit):
        with self.connect_db.cursor() as cursor:
            cursor.execute(db_command["Insert"]%(username, newhabit[0], newhabit[1], newhabit[2], newhabit[3], newhabit[4]))
            self.connect_db.commit()
    
    # Delete user's file from sql 
    # @username : user's name
    # @eraseHabit : habit to be deleted
    # @return : None
    def deleteHabit(self, username, erasehabit):
        with self.connect_db.cursor() as cursor:
            cursor.execute(db_command["Delete"]%(username, erasehabit))
            self.connect_db.commit()   
    
    # Read user's file from sql 
    # @username : user's name
    # @newHabit : habit to be inserted
    # @return : List of Habit which are user's habits
    def readHabit(self, username):
        with self.connect_db.cursor() as cursor:
            cursor.execute(db_command["Read"]%username)
            result = cursor.fetchall() 
        return result
    
    # Update user's file from sql 
    # @username : user's name
    # @updatehabit : habit to be updated
    # @return : None
    def updateHabit(self, username, updatehabit):
        with self.connect_db.cursor() as cursor:
            cursor.execute(db_command["Update"]%(username, updatehabit[1], updatehabit[2], updatehabit[3], updatehabit[4], updatehabit[0]))
            self.connect_db.commit() 
    
    # Close MySQL connection
    # @return : None
    def closeConnection(self):
        self.connect_db.close()
        