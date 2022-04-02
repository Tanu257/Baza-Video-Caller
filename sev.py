import socket
from threading import Thread
import time
import cv2
import pickle
from tkinter import *

title_windw = "Baza Video Call Service"
Window_Number = 0
port = 0
port_s = 0
ip = " "
Agents = []
frame_Delay = 0.05
client_sock = socket.socket()   

firstWind = Tk()
firstWind.title(title_windw)
def choosed_Window(winCode):
    global Window_Number
    Window_Number = winCode

    firstWind.destroy()

Label(text="Welcome to Baza Video call").grid(column=1,row=0)

Create_lB =Button(firstWind,text="Create Room",command=lambda: choosed_Window(0)).grid(column=1,row=1)
Join_lB = Button(firstWind,text="Join Room",command=lambda: choosed_Window(1)).grid(column=1,row=2)

firstWind.mainloop()
# Second Window (0 for create; 1 for Join)
def Server_Func():
    server_sock.bind((ip_s,port_s))
    server_sock.listen(5)

    Thread(target=(Accepting)).start()
    Thread(target=(Recive_0)).start()
    Thread(target=(Recive_1)).start()
    Server_Side_Agent()

def Server_Side_Agent():
    cap = cv2.VideoCapture(0)
    client_sock.connect((ip_s, port_s))
    def sending():
        while True:
            time.sleep(frame_Delay)
            cpps,readed_web = cap.read()
            client_sock.send(pickle.dumps(readed_web))
    def showing_servesre_side_client():
        while True:
            try:
                time.sleep(frame_Delay)

                g = client_sock.recv(208480524)
                huh = pickle.loads(g)

                cv2.imshow('erver side client', huh)
                
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            except:
                pass
    
    Thread(target=(sending)).start()
    Thread(target=(showing_servesre_side_client)).start()


def Accepting():
    while True:

        sok,addr = server_sock.accept()
        Agents.append(sok)



def Recive_0():
    while True:
        try:
            time.sleep(frame_Delay)
            gotData = Agents[0].recv(208480524)
            Agents[1].send(gotData)
        except:
            pass

def Recive_1():
    while True:
        try:
            time.sleep(frame_Delay)
            gotData = Agents[1].recv(208480524)
            Agents[0].send(gotData)
        except:
            pass

if(Window_Number == 0):

    server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    ip_s = socket.gethostbyname(socket.gethostname())

    root = Tk()
    def afterThat():
        global port_s
        port_s = int(portEntry.get())
        root.destroy()
    root.title(title_windw)
    Label(text="Welcome to Grand Video call").grid(column=1,row=0)
    Label(text="Enter Port Number Between 5000 To 45000").grid(column=0,row=1)
    portEntry = Entry(root)
    portEntry.grid(column=1,row=1)
    lb_addreds =Label(root,text=ip_s).grid(column=1,row=2)
    but_1 = Button(root,text="Start",command=afterThat).grid(column=1,row=3)
    root.mainloop()

    Server_Func()

def noramlized_client():
    cap = cv2.VideoCapture(1)
    client_sock.connect((ip, port))
    def sending():
        while True:
            time.sleep(frame_Delay)
            cpps,readed_web = cap.read()
            client_sock.send(pickle.dumps(readed_web))

    def showing_servesre_side_client():
        while True:
            try:
                time.sleep(frame_Delay)

                g = client_sock.recv(208480524)
                huh = pickle.loads(g)

                cv2.imshow('real client', huh)
                
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            except:
                pass
    
    Thread(target=(sending)).start()
    Thread(target=(showing_servesre_side_client)).start()

if(Window_Number == 1):


    client_window = Tk()
    client_window.title(title_windw)
    def confss():
        global port
        global ip

        port = int(portEntry.get())
        ip = lb_addreds.get()

        client_window.destroy()


    Label(text="Welcome to Grand Video call").grid(column=1,row=0)
    Label(text="Port :- ").grid(column=0,row=1)
    Label(text="Address :- ").grid(column=0,row=2)

    portEntry = Entry(client_window)
    portEntry.grid(column=1,row=1)
    lb_addreds =Entry(client_window)
    lb_addreds.grid(column=1,row=2)
    but_1 = Button(client_window,text="Start",command=confss).grid(column=1,row=3)

    client_window.mainloop()
    
    noramlized_client()

    # Finelly!!... It Ended!!..