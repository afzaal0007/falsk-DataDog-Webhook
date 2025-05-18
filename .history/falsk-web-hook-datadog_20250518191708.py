


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
