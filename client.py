from socket import *
import threading
import sys
#from playsound import playsound

#server code
FLAG = False

def send_to_server(clsock):
      global FLAG
      while True:
            if FLAG == True:
                  break
            send_msg = input('')
            clsock.sendall(send_msg.encode())

def recv_from_server(clsock):
      global FLAG
      while True:
            data = clsock.recv(1024).decode()
            if data == 'q':
                  print('Closing connection (press ENTER to exit)')
                  FLAG = True
                  break
# to add ringtone
#            playsound('alert.wav')
            print('server: ' + data)
            
def main(host):
    try:
          threads = []
      
          HOST = host
          PORT = 6789

          clientSoket = socket(AF_INET,SOCK_STREAM)
          clientSoket.connect((HOST,PORT))

          print('Client is connected to a chat server!\n')
          t_send = threading.Thread(target=send_to_server, args=(clientSoket,))
          t_rcv = threading.Thread(target=recv_from_server, args=(clientSoket,))

          threads.append(t_rcv)
          threads.append(t_send)
          t_rcv.start()
          t_send.start()
          
          t_rcv.join()
          t_send.join()

          print('EXITING')
          sys.exit()
          
    except ConnectionRefusedError:
        print('-'*60)
        print('server disconnected')
        
if __name__=='__main__':
    print('Terminal messenger (client)')
    print('-'*60)
    host = str(input('enter host: '))
    main(host)
