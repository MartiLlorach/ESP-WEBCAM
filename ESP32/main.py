import socket
import camera
import json

config = json.loads(open('config.json', 'r').read())
desktop_address = config['desktop_address']
desktop_udp_port = config['desktop_udp_port']
print("udp config: " + str(desktop_address) + ":" + str(desktop_udp_port))

# camera
camera.init(0, format=camera.JPEG)
camera.framesize(camera.FRAME_CIF)
camera.quality(30)
print("camera initialized")

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    img_buffer = camera.capture()
    udp_socket.sendto(img_buffer, (desktop_address, desktop_udp_port))