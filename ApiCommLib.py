import socket
import json
import sys


class JsonFunction:
    def __init__(self, functionName):
        json_string = '''{
            "functionName": "",
            "parameters":[
            ]
        }'''
        self.jsondata = json.loads(json_string)
        self.jsondata['functionName'] = functionName
        self.parameters = self.jsondata['parameters']

    def addParameter(self, name, value):
        self.parameters.append({"name": name, "value": value})

    def getBytes(self):
        return json.dumps(self.jsondata).encode('UTF-8')


class ApiComm:

    def __init__(self, ip, port):
        self.TCP_SERVER_IP = ip
        self.TCP_SERVER_PORT = port
        self.connectCount = 0
        self.connectServer()

    def connectServer(self):
        try:
            if self.connectCount <= 3:
                self.sock = socket.socket()
                self.sock.connect((self.TCP_SERVER_IP, self.TCP_SERVER_PORT))
                print(u'Client socket is connected with Server socket [ TCP_SERVER_IP: ' + self.TCP_SERVER_IP + ', TCP_SERVER_PORT: ' + str(self.TCP_SERVER_PORT) + ' ]')
                self.connectCount = 0
            else:
                print(u'Connect fail %d times.' % (self.connectCount))
                self.sock = None
        except Exception as e:
            print(e)
            self.connectCount += 1
            print(u'%d times try to connect with server'%(self.connectCount))
            self.connectServer()

    def senddata(self, data : bytes):
        if self.sock != None:
            print('send data size', len(data))
            length_bytes = len(data).to_bytes(4, "little")
            print('send bytes ', self.sock.send(length_bytes))
            print('send bytes ', self.sock.send(data))

    def disconnectServer(self):
        if self.sock != None:
            self.sock.close()
            self.sock = None

    def recvall(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def recvdata(self):
        if self.sock != None:
            length_bytes = self.recvall(self.sock, 4)
            length = int.from_bytes(length_bytes, byteorder='little')
            print('recv data size ', length)
            if length > 0:
                data = self.recvall(self.sock, int(length))
                return data
            return None
        else:
            return None
