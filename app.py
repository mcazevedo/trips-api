from flask import Flask, jsonify, request
import os
import pyodbc

app = Flask(__name__)

@app.route('/weekly_average_trips')
def get_weekly_average_trips():
    # Get the start and end dates from the query string parameters
    start_date = request.args.get('start_date', default='2018-05-01', type=str)
    end_date = request.args.get('end_date', default='2018-06-01', type=str)

    # Get the environment variables for the database connection
    server_name = os.environ.get('DB_SERVER_NAME')
    database_name = os.environ.get('DB_NAME')
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD')

    # Construct the connection string using the environment variables
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server_name};"
        f"DATABASE={database_name};"
        f"UID={username};"
        f"PWD={password}"
    )

    # Set up the connection to SQL Server database
    conn = pyodbc.connect(conn_str)

    # Create a cursor object to execute the stored procedure
    cursor = conn.cursor()
    params = (start_date, end_date)
    cursor.execute("{CALL GetWeeklyAverageTrips(?, ?)}", params)

    # Fetch the results and store them in a list of dictionaries
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    # Close the connection
    conn.close()

    # Return the results as JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run()
