import logging
# Configure logging to write to a file, appending new logs to the existing file

logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method
logging.info("Program ended")  # add this at the end of the main method

import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
 # use the pandas DataFrame to_sql() method to insert data
 # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()



sql_file = pathlib.Path( "matche.sql")  
try:
    with sqlite3.connect(db_file) as conn:
        sql_file = pathlib.Path("matches.sql")
        with open(sql_file, "r") as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print("Tables created successfully.")
except sqlite3.Error as e:
    print("Error creating tables:", e)

game_data_path = pathlib.Path("data", "game.csv")  # Check if this is correct

# Define the database file in the current root project directory
import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("score.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("matchdetails.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)
try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("matches.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
except sqlite3.Error as e:
        print("Error creating tables:", e)
def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        game_data_path = pathlib.Path("data", "game.csv")
        gamesdetails_data_path = pathlib.Path("data", "gamesdetails.csv")
        game_df = pd.read_csv(game_data_path)
        gamesdetails_df = pd.read_csv(gamesdetails_data_path)
        with sqlite3.connect(db_file) as conn:
# use the pandas DataFrame to_sql() method to insert data
# pass in the table name and the connection
            game_df.to_sql("games", conn, if_exists="replace", index=False)
            gamesdetails_df.to_sql("gamesdetails", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()

import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("score.db")

def query_data():
    """Function to execute a SQL SELECT query and print the result"""
    try:
        with sqlite3.connect(db_file) as conn:
 # Use pandas to read the result of the query into a DataFrame
            result_df = pd.read_sql_query ( "SELECT * FROM game;", conn)

            result_df2 = pd.read_sql_query("SELECT * FROM game WHERE id = 5;", conn)

            result_df2 = pd.read_sql_query("SELECT * FROM game ORDER BY date asc", conn)

            result_df2 = pd.read_sql_query("SELECT COUNT(*) FROM gamesdetails",conn)

            result_df2 = pd.read_sql_query("SELECT COUNT(*) FROM game",conn)

            result_df2 = pd.read_sql_query 
            ("DELETE FROM games WHERE city = Pune ",conn) 

            result_df2 = pd.read_sql_query
            ("SELECT * FROM  ORDER BY city DESC",conn)

            



 # Print the result DataFrame
            print(result_df)
    except sqlite3.Error as e:
        print("Error querying data:", e)

def main():
    query_data()

if __name__ == "__main__":
    main()
