import socket
import random
import threading
import csv

rows = []
with open("data.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        rows.append(row)

def Main():
    host  = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))
    s.listen(10)

    while True:
        c, addr = s.accept()
        print ('connection from : '+ str(addr))
        initial = 'welcome to mark attendance'
        c.send(str(initial).encode())
        threading.Thread(target = rollnumber, args = (c, addr)).start()


def rollnumber(c, addr):
    index = 0
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print ("from connected user : " + str(data))
        for each in rows:
            if each[0] == str(data):
                index = rows.index(each)
                break
        if index == 0:
            message = "ROLL NUMBER NOT FOUND"
            c.send(str(message).encode())
        else:
            c.send(("SECRET QUESTION" + str(rows[index][1])).encode())
            response = c.recv(1024)
            if rows[index][2] == response.decode():
                final_message = "ATTENDANCE SUCCESS"
                c.send(str(final_message).encode())
                break
            else:
                final_message = "ATTENDANCE FAILURE"
                c.send(str(final_message).encode())
    print("server closed from" + str(addr))
    c.close()

if __name__ == '__main__':
    Main()