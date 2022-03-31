import sys
import socket
import subprocess
from datetime import datetime

# Start with a clean screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Scan start time
t1 = datetime.now()

# Basic error handling

try:
    for port in range(1,995):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Finish time
t2 = datetime.now()

total =  t2 - t1

print 'Total Scan time: ', total