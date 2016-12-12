import urllib2
import socket


try:
    f = urllib2.urlopen(url="http://localhost:9999/myname")
    print f.read()
except socket.timeout:
    print "TIME OUT"
except urllib2.URLError:
    print "CONNECTION FAIL"

