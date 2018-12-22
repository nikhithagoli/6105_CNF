import socket
def main():
    host  = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.connect((host,port))
    initial = s.recv(1024)
    print('received from server : '+ initial.decode())
    message = input("MARK ATTENDANCE : ")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024)
        if(data.decode() == "ROLL NUMBER NOT FOUND"):
            print(str(data.decode()))
            break
        else:
            print(str(data.decode()))
            answer = input("SECRET ANSWER : ")
            s.send(answer.encode())
            response = s.recv(1024).decode()
            if(response == "ATTENDANCE SUCCESS"):
                print(str(response))
                break
    s.close()


if __name__ == "__main__":
    main()