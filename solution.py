from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e .g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = '127.0.0.1:1025'
    mailport = 25
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((mailserver, mailport))

    # Fill in start
    # Fill in end

    recv = clientsocket.recv(1025).decode()
    print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    helocommand = 'HELO Alice\r\n'
    clientsocket.send(helocommand.encode())
    recv1 = clientsocket.recv(1025).decode()
    print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromcommand = "MAIL FROM: <ol2089@nyu.edu>\r\n"
    clientsocket.send(mailfromcommand.encode())
    recv1 = clientsocket.recv(1025)
    print(recv1)
    #if recv1[:3] != '250':
        #print('mail from 250 reply not received from server.')

    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcpttocommand = 'RCPT TO: <ol2089@nyu.edu>\r\n'
    clientsocket.send(rcpttocommand.encode())
    recv1 = clientsocket.recv(1025)
    print(recv1)
    #if recv1[:3] != '250':
        #print('rcpt to 250 reply not received from server.')

    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n"
    clientsocket.send(data.encode())
    recv4 = clientsocket.recv(1025)
    print("After DATA command: Hello everyone " + recv4)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in start

    # Fill in end

    # Message ends with a single period.
    # Fill in start

    subject = "Subject: SMTP mail client testing \r\n\r\n"
    clientsocket.send(subject.encode())
    message = raw_input("Enter your message: hi \r\n")
    clientsocket.send(message.encode())
    clientsocket.send(endmsg.encode())
    #print("Response after sending message body:" + recv_msg.decode())
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitcommand = 'Quit\r\n'

    clientsocket.send(quitcommand)
    recv1 = clientsocket.recv(1024)
    print(recv1)
    #if recv1[:3] != '250':
        #print('end msg 250 reply not received from server.')

    clientsocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
