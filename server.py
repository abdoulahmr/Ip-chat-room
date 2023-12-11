from socket import *
import threading
import sys

#server code
FLAG = False

def recv_from_client(conn):
      global FLAG
      try:
            
            while True:
                  if FLAG == True:
                        break
                  message = conn.recv(1024).decode()

                  if message == 'q':
                        conn.send('q'.encode())
                        print('Closing connection (press ENTER to exit)')
                        conn.close()
                        FLAG = True
                        break
# to add ringtone
#                  playsound('alert.wav')
                  print('Client:'+ message)

      except:
            conn.close()

def send_to_client(conn):
      global FLAG
      try:
            
            while True:
                  if FLAG == True:
                        break
                  send_msg = input('')

                  if send_msg == 'q':
                        conn.send('q'.encode())
                        print('Closing connection (press ENTER to exit)')
                        conn.close()
                        FLAG = True
                        break
                  conn.send(send_msg.encode())
      except:
            conn.close()

def main(host):
      threads = []
      global FLAG

      HOST = host
      serverPort = 6789

      serverSocket = socket(AF_INET, SOCK_STREAM)

      serverSocket.bind((HOST, serverPort))
      
      serverSocket.listen(1)

      print('The chat server is ready to connect to a chat client')

      connectionSocket, addr = serverSocket.accept()

      print('Server is connected with a chat client\n')

      t_rcv = threading.Thread(target=recv_from_client, args=(connectionSocket,))
      t_send = threading.Thread(target=send_to_client, args=(connectionSocket,))

      threads.append(t_rcv)
      threads.append(t_send)
      t_rcv.start()
      t_send.start()

      t_rcv.join()
      t_send.join()

      print('EXITING')
      serverSocket.close()

      sys.exit()

if __name__=='__main__':
    print('Terminal messenger (server)')
    print('-'*60)
    host = str(input('enter host: '))
    main(host)
