## Trips API
This is a Flask-based API that retrieves the weekly average number of trips by region between two specified dates from a Microsoft SQL Server database. The project includes a Dockerfile that creates a Docker image of the application, a SQL script for the stored procedure that retrieves the data, and a requirements.txt file that lists the Python dependencies.

### Requirements
Python 3.9 or later
Docker
Microsoft SQL Server ODBC Driver 17 for Linux
Installation
Clone the repository:


 ``$ git clone https://github.com/<username>/trips-api.git``
Change into the project directory:



 ``$ cd trips-api``

Create a virtual environment:


``$ python -m venv venv``

Activate the virtual environment:


``$ source venv/bin/activate``

Install the dependencies:


``$ pip install -r requirements.txt``


### Running the API Locally
Set the environment variables for the database connection:

``$ export DB_SERVER_NAME=<server_name>``
``$ export DB_NAME=<database_name>``
``$ export DB_USERNAME=<username>``
``$ export DB_PASSWORD=<password>``


Start the Flask development server:


``$ python app.py``
The server will start listening on http://localhost:5000/.

Test the API by accessing the following URL in your web browser or using curl:


http://localhost:5000/weekly_average_trips?start_date=2018-05-01&end_date=2018-06-01

This will return the weekly average number of trips by region between May 1, 2018, and June 1, 2018.

### Running the API in Docker
Build the Docker image:


``$ docker build -t trips-api .``

Run the Docker container:


`$ docker run -p 5000:5000 \`
 ` -e DB_SERVER_NAME=<server_name> \`
 ` -e DB_NAME=<database_name> \`
 ` -e DB_USERNAME=<username> \`
 `-e DB_PASSWORD=<password> \`
  `trips-api`


Test the API by accessing the following URL in your web browser or using curl:


http://localhost:5000/weekly_average_trips?start_date=2018-05-01&end_date=2018-06-01
This will return the weekly average number of trips by region between May 1, 2018, and June 1, 2018.

### SQL Script
The sql/GetWeeklyAverageTrips.sql file contains the SQL script for the stored procedure that retrieves the data used by the API. The stored procedure takes two parameters: @startDate and @endDate. The script creates a common table expression (CTE) to calculate the average number of trips per week by region and then selects the data for the specified date range.