from socket import *
import time
import base64


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e .g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect(mailserver, port)

    # Fill in start
    # Fill in e nd

    recv = clientsocket.recv(1024).decode()
    # print(recv)
    # if recv[:3] != '220':
    # print('220 reply not received from server.')

    # Send HELO command and print server response.
    helocommand = 'HELO Alice\r\n'
    clientsocket.send(helocommand.encode())
    recv1 = clientsocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    # print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromcommand = "MAIL FROM: <ol2089@nyu.edu>\r\n"
    clientsocket.send(mailfromcommand.encode())
    recv1 = clientsocket.recv(1024)
    # print(recv2)
    # if recv2[:3] != '250':
    # print('mail from 250 reply not received from server.')

    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcpttocommand = 'RCPT TO: <mayowa.labinjo@yahoo.com>\r\n'
    clientsocket.send(rcpttocommand.encode())
    recv1 = clientsocket.recv(1024).decode()
    # print(recv3)
    # if recv3[:3] != '250':
    # print('rcpt to 250 reply not received from server.')

    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n"
    clientsocket.send(data.encode())
    recv1 = clientsocket.recv(1024).decode()

    # print("After DATA command: " + recv4)
    # if recv1[:3] != '250':
    # print('250 reply not received from server.')
    # Fill in start

    # Fill in end

    # Message ends with a single period.
    # Fill in start

    clientsocket.send(msg.encode())

    clientsocket.send(endmsg.encode())
    recv1 = clientsocket.recv(1024).decode()
    #print("Response after sending message body:" + recv_msg.decode())
    # if recv1[:3] != '250':
    # print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit = 'QUIT\r\n'
    clientsocket.send(quit.encode())
    message = clientsocket.recv(1024).decode()
    recv1 = clientsocket.recv(1024).decode()
    #print (recv1)

    # if recv1[:3] != '250':
    # print('end msg 250 reply not received from server.')

    # Fill in end
    clientsocket.close()

    if __name__ == '__main__':
        smtp_client(1025, '127.0.0.1')
