"""This program connects to an NTP server and displays the current time on screen."""
from contextlib import closing
from socket import socket, AF_INET, SOCK_DGRAM
from struct import calcsize, unpack
from time import ctime


def main():
    packet_format = '!12I'
    payload = b'\x1b' + 47 * b'\0'
    host = 'pool.ntp.org'
    port = 123
    with closing(socket(AF_INET, SOCK_DGRAM)) as connect:
        connect.sendto(payload, (host, port))
        message, addr = connect.recvfrom(1024)
    data = unpack(packet_format, message[0:calcsize(packet_format)])
    time = data[10] + float(data[11]) / 2 ** 32 - 2208988800
    print(ctime(time).replace('  ', ' '))


if __name__ == '__main__':
    main()