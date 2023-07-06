# **rpi-monitor-api**
A simple flask app that serves up an api to help monitor the storage and performance of a raspberry pi.

## Use Case
**Example of sensors created in a [Home Assistant](https://www.home-assistant.io/) dashboard reading from the api**

![alt text](/img/haDash.PNG)

**Sample API Output**

```json
{
    "cputemp": 47.2,
    "cpupc": 28.3,
    "mempc": 54.21,
    "share": {
        "total": 915.6,
        "used": 56.3,
        "free": 400.1
    },
    "root": {
        "total": 233.4,
        "used": 13.24,
        "free": 202.5
    }
}
```
## Requirements

- Python 3.x
- pip (Python package installer)
- Python Packages:
  - psutil 
  - flask 
  - flask-restful 
  - gpiozero

## Usage

In the command-line interface of your Pi, create yourself a project directory and download/clone the monitor.py file. 

Open the file and customize the local ip address of your pi, the port you want to publish to, and directories you want to monitor.

From the project directory, Run the Flask application:

```shell
python3 monitor.py
```
The Flask API will start running on http://localhost:9000/. 

To access the metrics, send a GET request to http://localhost:9000/ or use the appropriate URL based on your host and port configuration.

The API will respond with a JSON object containing the system metrics, including CPU temperature, CPU utilization, and total/used/free storage for the folders you want to monitor.

You can integrate this API with other applications or services to monitor system metrics or trigger automation based on the received data.

To stop the Flask application, press Ctrl+C in the command-line interface.

To run the script in the background on startup, add the following to your crontab.

```shell
# Run monitor.py a minute after startup
@reboot sleep 60 && sudo /usr/bin/python3 /[full project path]/monitor.py & 
```
## Customization

You can modify the code in monitor.py to include additional metrics or customize the behavior of the API as per your requirements.

Update the subdirectories, host, and port in the code to match your desired paths and network configuration.

If you don't care about temperature, the code can also be modified for use on linux machines by removing reference to/metrics generated from the gpiozero package.