# scan local open ports with nc -zv localhost 1-65000 2>&1 | grep succeeded

## get the flag by connecting to the service running in this port
nc localhost 6969