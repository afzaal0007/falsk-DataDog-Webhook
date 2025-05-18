from flask import Flask, request, jsonify
import os
import shutil
import datadog

app = Flask(__name__)

# Set up Datadog API credentials
datadog_api_key = "YOUR_DATADOG_API_KEY"
datadog_app_key = "YOUR_DATADOG_APP_KEY"

# Set up log folder path and threshold
log_folder_path = "/path/to/CustomWebApplication/logs"
threshold = 90  # percentage of disk usage to trigger alert

@app.route('/datadog_webhook', methods=['POST'])
def datadog_webhook():
    # Get the event data from Datadog
    event_data = request.get_json()

    # Check if the event is related to the CustomWebApplication log folder
    if event_data['event']['source'] == 'CustomWebApplication' and event_data['event']['resource'] == log_folder_path:
        # Get the disk usage percentage of the log folder
        disk_usage = get_disk_usage(log_folder_path)

        # Check if the disk usage is above the threshold
        if disk_usage > threshold:
            # Trigger an alert in Datadog
            trigger_alert(event_data['event']['title'], event_data['event']['text'])

            # Clean the log folder
            clean_log_folder(log_folder_path)

    return jsonify({'status': 'ok'})

def get_disk_usage(path):
    # Get the disk usage percentage of the given path
    total, used, free = shutil.disk_usage(path)
    return (used / total) * 100

def trigger_alert(title, text):
    # Trigger an alert in Datadog using the API
    datadog.api.Event.create(title=title, text=text, tags=['CustomWebApplication'])

def clean_log_folder(path):
    # Clean the log folder by deleting files older than 30 days
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path) and file.endswith('.log'):
            file_age = (datetime.now() - datetime.fromtimestamp(os.path.getctime(file_path))).days
            if file_age > 30:
                os.remove(file_path)

if __name__ == '__main__':
    app.run(debug=True)