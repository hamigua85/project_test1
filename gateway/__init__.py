import socket
import threading
from app import redis
import time


class Gateway:
    def __init__(self):
        try:
            self.__buf_size = 1024
            self.__server_addr = ('0.0.0.0', 8888)
            self.__server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.__server.bind(self.__server_addr)
        finally:
            pass

    def __rec(self):
        while True:
            data, client_addr = self.__server.recvfrom(self.__buf_size)
            rec_data = []
            for d in data:
                rec_data.append(ord(d))
            redis.set(client_addr, rec_data, 5)

    def create_gateway(self):
        t1 = threading.Thread(target=self.__rec)
        t1.start()
