import sqlite3
import os

def get_names_from_db():
    db_file = "database/user_database.db"
    conn = sqlite3.connect(db_file)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    query = "SELECT * FROM tbl_user_info"

    data_dictionary = {}

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if rows:
            for row in rows:
                data_dictionary[row["PIN"]] = dict(row)
        else:
            print("No data found.")

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if conn:
            conn.close()
    
    return data_dictionary

def create_dictionary_file(data_dictionary, file_name):
    folder_path = "database"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, "w") as f:
        f.write("user_data = {\n")
        for key, value in data_dictionary.items():
            f.write(f'    "{key}": {value},\n')
        f.write("}\n")

def main():
    data_dictionary = get_names_from_db()
    if data_dictionary:
        file_name = "user_data.py"
        create_dictionary_file(data_dictionary, file_name)
        print(f"Dictionary file '{file_name}' created successfully in the 'database' folder.")
    else:
        print("No data retrieved from the database.")

if __name__ == "__main__":
    main()
