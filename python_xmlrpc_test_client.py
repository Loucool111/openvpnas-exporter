from http.client import HTTPConnection
import socket
from xmlrpc import client

class UnixStreamHTTPConnection(HTTPConnection):
    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(self.host)

class UnixStreamTransport(client.Transport, object):
    def __init__(self, socket_path):
        self.socket_path = socket_path
        super(UnixStreamTransport, self).__init__()

    def make_connection(self, host):
        return UnixStreamHTTPConnection(self.socket_path)

proxy = client.ServerProxy('http://localhost', transport=UnixStreamTransport("/usr/local/openvpn_as/etc/sock/sagent.localroot"))

print("GetVPNSummary():")
print(proxy.GetVPNSummary())

print("GetSubscriptionStatus()")
print(proxy.GetSubscriptionStatus())