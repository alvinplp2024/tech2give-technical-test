#QUESTION 1

import pyodbc

def get_race_results():
    try:
        # Defining the database connection details
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=localhost;'
            'DATABASE=RaceResultsDB;'  # Database name
            'UID=alvin;'  # Username for database
            'PWD=alvin123;'  # Password for database
        )
        
        print("Connected to database successfully.")
        
        cursor = conn.cursor()

        # SQL query to select 2020 data in the specified order
        query = """
        SELECT location, grid, position, fastest_lap, points, driver_name, race_name, time, race_year, team_name, race_date
        FROM dbo.results  -- Make sure `results` is the actual table name
        WHERE race_year = 2020
        ORDER BY points DESC;
        """

        # Executing the above query
        cursor.execute(query)

	#if query executed successfully it will output
        print("Query executed successfully.")

        # Fetching all results
        results = cursor.fetchall()

        # Displaying the results or notify if no data found
        if results:
            print("Displaying results:")
            for row in results:
                print(row)
        else:
            print("No results found for the specified year.")

    except pyodbc.Error as e:
        print("Database error:", e)

    finally:
        # Closing the connection
        conn.close()
        print("Database connection closed.")

# Call the function to display results
get_race_results()
