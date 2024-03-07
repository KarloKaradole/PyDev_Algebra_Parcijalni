import sqlite3

def get_names_from_db():
    
    db_file = "database/user_database.db"
    conn = sqlite3.connect(db_file)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    query = "SELECT * FROM tbl_user_info"

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if rows:
            for row in rows:
                print(dict(row))  
        else:
            print("No data found.")

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if conn:
            conn.close()
        
def get_user(db_file, person_name):
    
    db_file = "database/user_database.db"
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row  

    cursor = conn.cursor()

    query = "SELECT * FROM tbl_user_info WHERE PIN = ?"

    try:
        cursor.execute(query, (person_name,))

        row = cursor.fetchone()
        
        if row:
            print(dict(row))  
        else:
            print(f"No data found for {person_name}.")

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if conn:
            conn.close()
