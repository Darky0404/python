from socket import *
import time
s = socket(AF_INET, SOCK_STREAM)
s.bind(('',8888))
s.listen(5) 
while True:
    client,addr = s.accept()
    print("Получен запрос от %s" % str(addr))
    timestr = time.ctime(time.time()) + "\r\n"
    client.send(timestr.encode('ascii'))
    client.close()
