import time
import network
import esp
import gc
import json

# disable debugging
esp.osdebug(None) 

# run garbage collection
gc.collect() 

# get configuration from file
config = json.loads(open('config.json', 'r').read())

# connect to wifi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(config['ssid'], config['password'])

# wait for wifi connection
print('Connecting to network', end='')
while not station.isconnected():
    time.sleep(0.5)
    print('.', end='')
    pass
print('\nNetwork config:', station.ifconfig())
