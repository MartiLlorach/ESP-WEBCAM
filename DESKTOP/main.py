import tkinter as tk
from PIL import ImageTk
import socket


udp_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server.bind(("", 8888))


def recieve_image():
    global image_label, udp_server

    bytesAddressPair = udp_server.recvfrom(102400)  # 100kb
    imgBytes = bytesAddressPair[0]

    img = ImageTk.PhotoImage(data=imgBytes)
    image_label.configure(image=img)
    image_label.image = img
    window.after(1, recieve_image)


window = tk.Tk()
window.title("ESP32-WEBCAM")
window.geometry("240x240")


image_label = tk.Label(window)
image_label.place(x=0, y=0, relwidth=1, relheight=1)


recieve_image()
window.mainloop()
