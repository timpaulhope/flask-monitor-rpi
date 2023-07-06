# ==
# Please visit https://github.com/timpaulhope/rpi-monitor-api for readme + config details
#
# Running this flask app on a Raspberry will create a simple api endpoint on port 9000 displaying:
# + CPU temperature
# + CPU utalization
# + File system utalization for
#   + the root drive; and
#   + Mounted External Drives
# == 

import psutil
from flask import Flask
from flask_restful import Resource, Api
from gpiozero import CPUTemperature

## == Setup ====
app = Flask(__name__)
api = Api(app)
strLocalIp = '0.0.0.0'          ## <- Better to set to fixed IP of the device
valPort = 9000                  ## <- Change port here if 9000 is already in use
BytesPerGB = float(1024.0 ** 3) ## <- A Factor to convert Bytes to Gb
SecondBetweenUpdates = 5.0      ## <- Sets pause between updates (Should be greater than 2)
# == This generates/updates the json packet sent to the api ===
class JsonOut(Resource):
    def get(self):
        # Yes, yes, I know It's an endless loop but the sleep needs to happen
        # between updates to reduce the occasional error
        while True:
            try:
                cpu = CPUTemperature()         ## get cpu temp
                cpuPc = psutil.cpu_percent()   ## get cpu utalization
                mem = psutil.virtual_memory()  ## get mem less swap

                ## Set folders you want to monitor here
                rootFolder = psutil.disk_usage('/')
                shareFolder = psutil.disk_usage('/mnt/share')
                ## NOTE: You can keep on adding folders here as needed
                ## additionalFolders = psutil.disk_usage('/mnt/XXXXX')

                # == Set default out packet content ====
                return {'cputemp': round(float(cpu.temperature),1),
                        'cpupc': float(cpuPc),
                        'mempc': round(100 * (float(mem.used) / float(mem.total)),2),
                        'share': {'total' : round( float(shareFolder.total) / BytesPerGB ,1),
                                'used' : round( 100 * (float(shareFolder.total - shareFolder.free) / float(shareFolder.total)) ,2),
                                'free' : round(float(shareFolder.free) / BytesPerGB ,1)},
                        'root': {'total' : round(float(rootFolder.total) / BytesPerGB ,1),
                                'used' : round(100*(float(rootFolder.total - rootFolder.free) / float(rootFolder.total)) ,2),
                                'free' : round(float(rootFolder.free) / BytesPerGB ,1)}}

            # Handle the occasional runtime error
            except RuntimeError as e:
                return {"RuntimeError"}
                time.sleep(SecondBetweenUpdates)
                continue

        time.sleep(SecondBetweenUpdates)

# == add the json as a resource ==
api.add_resource(JsonOut, '/')

if __name__ == "__main__":
    app.run(host=strLocalIp, port=valPort, debug=True)

# == EoF ==