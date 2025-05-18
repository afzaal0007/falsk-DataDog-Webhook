This Python script is a Flask application that defines a webhook endpoint. When a POST request is sent to this endpoint, the application performs the following actions:

Get the current date and time: It fetches the current date and time in a specific format.
Define the log directory: It specifies the directory where log files are stored.
List log files: It lists all files in the log directory that have a ".log" extension.
Delete log files: It attempts to delete each log file found in the directory.
Get POST data: It retrieves the data sent in the POST request as JSON.
Create a log entry: It creates a log entry containing the current timestamp and the POST data.
Log the entry: It writes the log entry to a specified log file in JSON format.
Run the Flask application: It runs the Flask application on host 0.0.0.0 and port 8080.


from flask import Flask, request
import datetime
import os
import json

app = Flask(__name__)

# Define a route to receive the webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the current date and time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Define the directory where log files are located
    log_directory = '/var/log/virtusa/'

    # List log files in the directory with the ".log" extension
    log_files = [f for f in os.listdir(log_directory) if f.endswith(".log")]

    # Delete log files
    for log_file in log_files:
        try:
            os.remove(os.path.join(log_directory, log_file))
        except Exception as e:
            return f'Error deleting log file: {str(e)}'

    # Get the POST data as JSON
    post_data = request.get_json()

    # Create a log entry with date, time, and POST data
    log_entry = {
        'timestamp': current_time,
        'post_data': post_data
    }

    # Log the entry in JSON format to the specified file
    log_file_path = '/var/www/html/resources/tmp/datetime.log'
    with open(log_file_path, 'a') as log_file:
        log_file.write(json.dumps(log_entry) + '\n')

    return 'Webhook received, log files deleted, and data logged.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
