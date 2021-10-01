from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailServer = 'smtp.nyu.edu'
    mailPort = 25
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailServer, mailPort))

    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
   # if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
   # if recv1[:3] != '250':
       # print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromCommand = 'MAIL FROM: <ol2089@nyu.edu>\r\n'
    clientSocket.send(mailfromCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    #if recv1[:3] != '250':
        #print('mail from 250 reply not received from server.')

    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcpttoCommand = 'RCPT TO: <ol2089@nyu.edu>\r\n'
    clientSocket.send(rcpttoCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
   # if recv1[:3] != '250':
        #print('rcpt to 250 reply not received from server.')

    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    print("After DATA command: " + recv4)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in start

    # Fill in end

    # Message ends with a single period.
    # Fill in start
    mailMessageEnd = '\r\n.\r\n'
    clientSocket.send(data + mailMessageEnd)
    recv1 = clientSocket.recv(1024)
    print(recv1)
   # if recv1[:3] != '250':
       # print('end msg 250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'Quit\r\n'
    clientSocket.send(quitCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    #if recv1[:3] != '250':
       # print('quit 250 reply not received from server.')

    clientSocket.close()


if __name__ != '__main__':
    pass
else:
    smtp_client(1025, '127.0.0.1')
