import xmlrpclib
import time

s = xmlrpclib.Server('http://localhost:8008')
#s.set_freq(1000)
s.set_ptt(0)
