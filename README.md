# **rpi-monitor-api**
A simple flask app that serves up an api to help monitor the storage and performance of a raspberry pi

## Use Case
**Example of API being used as sensors in a [Home Assistant](https://www.home-assistant.io/) dashboard**

![alt text](/img/haDash.PNG)

I call this api from an external home automation platform to create sensor entities for automations.

## Build

>**NOTE:** The following assumes you're running `python3` and have `pip3` installed on you're Pi.

The following are all run from the terminal of th Pi you want to monitor.

Install the packages used by the app.
```bash
pip3 install psutil flask flask-restful gpiozero
```

Use `nano` (or other text editor) to create a blank py script.
```bash
nano monitor.py
```
Copy/Paste the code from the `monitor.py` file in this repo in to the blank file and adjust the IP adress, port, and folders you want to monitor before saving the file.

Run the file locally to see if it works.
```bash
python3 monitor.py
```
All going well, you should see something like this in the terminal.
```bash
 * Serving Flask app 'monitor'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:9000
 * Running on http://192.16.20.36:9000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 755-306-531
```

Once up and running, open a browser and go to http://localhost:9000/ to view the output
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
