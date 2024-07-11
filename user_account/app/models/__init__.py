from app.db import Connection

class User:
    def __init__(self):
        self.db = Connection()
    def register_user(self, username, password):
        self.username = username
        self.password = password
        
        # user data 
        user =(self.username, self.password)
        
        check_query = "SELECT * FROM users WHERE username = %s "
        self.db.cursor.execute(check_query,[self.username])
        specific_user = self.db.cursor.fetchone()
    #   ensure you check if password == confirm password
        if specific_user:
            print("username already exist in database")
            return False
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
          # Execute query that inserts user data into the database
        record= self.db.cursor.execute(query, user)
        new_user = self.db.cursor.rowcount
        #  check if execution is successful
        if new_user:
            # commit data to database
            self.db.conn.commit()
        #  close cursor the cursor
        self.db.cursor.close()
        # close the connection
        self.db.conn.close()
        return record
            
    def login_user(self, username, password):
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.db.cursor.execute(query, [username, password])
        results = self.db.cursor.fetchone()
        self.db.cursor.close()
        self.db.conn.close()
        return results
    def update_password_By_username(self, username, password):
        '''Update users password by usernames'''
        self.username = username
        self.password = password
        query = "UPDATE users SET password = %s WHERE username = %s"
        self.db.cursor.execute(query, [self.password, self.username])
        result = self.db.cursor.rowcount
        if result:
            self.db.conn.commit()
        self.db.cursor.close()
        self.db.conn.close()
        return result
        
    def get_all_users(self):
        query = "SELECT * FROM users"
        self.db.cursor.execute(query)
        users = self.db.cursor.fetchall()
        return users  
    # delete user by username
 
        
        
