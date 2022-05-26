import socket
import time

host = "challenges.ctfd.io"
port = 30299

def main():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((host, port))
  print(client.recv(4096)).strip('\n')
  print("helo wallen@fit.edu\r")
  client.sendall("helo wallen@fit.edu\r\n")
  print(client.recv(4096)).strip('\n')
  print("MAIL FROM: cshoop2018@my.fit.edu\r")
  client.sendall("MAIL FROM: cshoop2018@my.fit.edu\r\n")
  print(client.recv(4096)).strip('\n')
  print("RCPT TO: wallen@fit.edu\r")
  client.sendall("RCPT TO: wallen@fit.edu\r\n")
  print(client.recv(4096)).strip('\n')
  print("DATA\r")
  client.sendall("DATA\r\n")
  time.sleep(.5)
  print(client.recv(4096)).strip('\n')
  print("From: cshoop2018@my.fit.edu\r\nTo: wallen@fit.edu\r\nSubject: CSE 3231 Assignment # 3\r\nDate: Sat, 21 Nov 2020 16:25:00 -0400 (EDT)\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset='us-ascii'\r\nContent-Transfer-Encoding: 7bit\r\nThis is an email test written in python.\r\n.\r")
  client.sendall("From: cshoop2018@my.fit.edu\r\n""To: wallen@fit.edu\r\n""Subject: CSE 3231 Assignment # 3\r\n""Date: Sat, 21 Nov 2020 16:025:00 -0400 (EDT)\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset='us-ascii'\r\nContent-Transfer-Encoding: 7bit\r\nThis is an email test written in python.\r\n.\r\n")
  time.sleep(.5)
  print(client.recv(4096)).strip('\n')
  print("QUIT\r")
  client.sendall("QUIT\r\n")
  print(client.recv(4096)).strip('\n')
  client.close()

if __name__ == "__main__":
  main()
