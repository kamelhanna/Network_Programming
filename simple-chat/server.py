from socket import *

s = socket(AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 7002

s.bind((host, port))

s.listen(5)

client, address = s.accept()

print("connection from", address[0])

while True: 
    received_data = client.recv(2048)
    if received_data.decode() == 'Q':
        break
    print("Client : ", received_data.decode('utf=8'))

    text_input = input("server : ")
    client.send(text_input.encode('utf=8'))
    if text_input == 'Q':
        break

s.close()
