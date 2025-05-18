# This Python script is a Flask application that defines a webhook endpoint. When a POST request is sent to this endpoint, the application performs the following actions:

# Get the current date and time: It fetches the current date and time in a specific format.
# Define the log directory: It specifies the directory where log files are stored.
# List log files: It lists all files in the log directory that have a ".log" extension.
# Delete log files: It attempts to delete each log file found in the directory.
# Get POST data: It retrieves the data sent in the POST request as JSON.
# Create a log entry: It creates a log entry containing the current timestamp and the POST data.
# Log the entry: It writes the log entry to a specified log file in JSON format.
# Run the Flask application: It runs the Flask application on host 0.0.0.0 and port 8080.
# The script listens for incoming POST requests on the /webhook endpoint. When a request is received, it performs the specified actions and returns a response.   

# This is a Python script that defines a Flask web application.
# The application listens for incoming POST requests on the /webhook endpoint.
# When a request is received, it performs several actions, including deleting log files and logging the POST data.

# Import the Flask library, which is a micro web framework for Python.
# The 'Flask' class is used to create a new Flask application instance.
# The 'request' object is used to access the data sent in the POST request.

from flask import Flask, request

# Import the datetime library, which provides classes for manipulating dates and times.
import datetime

# Import the os library, which provides a way to interact with the operating system.
# The 'os' library is used to delete log files and access the file system.
import os

# Import the json library, which provides a way to work with JSON data.
# The 'json' library is used to parse the POST data and log it in JSON format.
import json

# Create a new Flask application instance.
# The '__name__' variable is a built-in Python variable that refers to the current module name.
# In this case, it is used to create a new Flask application instance.
app = Flask(__name__)

# Define a route to receive the webhook.
# The '/webhook' path is the URL that the application will listen for incoming POST requests on.
# The 'methods' parameter specifies that the route should only respond to POST requests.
@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Handle POST requests to the /webhook endpoint.
    Deletes log files and logs the POST data with a timestamp.
    """
    
    # Get the current date and time.
    # The 'datetime.datetime.now()' function returns the current date and time.
    # The 'strftime' method formats the date and time as a string.
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Define the directory where log files are located.
    # The '/var/log/virtusa/' path is the directory where log files are stored.
    log_directory = '/var/log/virtusa/'

    # List log files in the directory with the ".log" extension.
    # The 'os.listdir' function returns a list of files in the directory.
    # The 'endswith' method filters the list to only include files with the ".log" extension.
    log_files = [f for f in os.listdir(log_directory) if f.endswith(".log")]

    # Delete log files.
    # The 'os.remove' function deletes a file.
    # The 'try' and 'except' blocks handle any errors that may occur when deleting files.
    for log_file in log_files:
        try:
            os.remove(os.path.join(log_directory, log_file))
        except Exception as e:
            # Return an error message if a file cannot be deleted.
            return f'Error deleting log file: {str(e)}'

    # Get the POST data as JSON.
    # The 'request.get_json' method parses the POST data as JSON.
    post_data = request.get_json()

    # Create a log entry with date, time, and POST data.
    # The 'log_entry' dictionary contains the current timestamp and the POST data.
    log_entry = {
        'timestamp': current_time,
        'post_data': post_data
    }

    # Log the entry in JSON format to the specified file.
    # The '/var/www/html/resources/tmp/datetime.log' path is the file where log entries are written.
    # The 'json.dumps' function converts the log entry to a JSON string.
    # The 'open' function opens the file in append mode.
    log_file_path = '/var/www/html/resources/tmp/datetime.log'
    with open(log_file_path, 'a') as log_file:
        log_file.write(json.dumps(log_entry) + '\n')

    # Return a success message.
    return 'Webhook received, log files deleted, and data logged.'