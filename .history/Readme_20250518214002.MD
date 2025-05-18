# CustomWebApplication Log Folder Monitor

This Flask application monitors the log folder of a CustomWebApplication and triggers an alert in Datadog when the folder is full. It also cleans the log folder by deleting files older than 30 days.

## Requirements

* Flask 2.x
* Datadog API credentials
* Python 3.8+

## Installation

1. Clone this repository: `git clone https://github.com/your-username/CustomWebApplication-Log-Folder-Monitor.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Datadog API credentials in `config.py`
4. Run the application: `flask run`

## Configuration

* `config.py`: Set up Datadog API credentials and log folder path
* `app.py`: Flask application code
* `requirements.txt`: Dependencies required by the application

## Diagram

Here is a high-level diagram of the application:

                              +---------------+
                              |  Datadog API  |
                              +---------------+
                                        |
                                        |
                                        v
                              +---------------+
                              |  Flask Webhook  |
                              |  (this application) |
                              +---------------+
                                        |
                                        |
                                        v
                              +---------------+
                              |  CustomWebApplication  |
                              |  Log Folder          |
                              +---------------+


                              The diagram shows the following components:

* Datadog API: receives alerts and triggers notifications
* Flask Webhook (this application): monitors log folder and triggers alerts in Datadog
* CustomWebApplication Log Folder: monitored by the Flask webhook

## Usage

1. Set up Datadog API credentials and log folder path in `config.py`
2. Run the application: `flask run`
3. The application will monitor the log folder and trigger alerts in Datadog when the folder is full
4. The application will also clean the log folder by deleting files older than 30 days

## Contributing

Contributions are welcome! Please submit a pull request with your changes.


@startuml
participant "Datadog API" as datadog
participant "Flask Webhook" as webhook
participant "CustomWebApplication Log Folder" as log_folder

datadog ->> webhook: Alert
webhook ->> log_folder: Monitor
log_folder ->> webhook: Disk usage
webhook ->> datadog: Alert
webhook ->> log_folder: Clean
@enduml