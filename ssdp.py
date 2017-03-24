import sys
import socket


def findAuroraURL():
  """
  Do an ssdp broadcast to find the URL of an Aurora device
  """
  SSDP_ADDR = "239.255.255.250";
  SSDP_PORT = 1900;
  SSDP_MX = 3;
  SSDP_ST = "nanoleaf_aurora:light";

  ssdpRequest = "M-SEARCH * HTTP/1.1\r\n" + \
                  "HOST: %s:%d\r\n" % (SSDP_ADDR, SSDP_PORT) + \
                  "MAN: \"ssdp:discover\"\r\n" + \
                  "MX: %d\r\n" % (SSDP_MX, ) + \
                  "ST: %s\r\n" % (SSDP_ST, ) + "\r\n";                

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.sendto(ssdpRequest, (SSDP_ADDR, SSDP_PORT))
  while True: 
    try:                
      response = sock.recv(1000)
      if SSDP_ST in response:
        for line in response.split("\n"):
          if "Location: " in line:
            return (line[len("Location: "):]).strip()
    except socket.timeout:
      break
  raise Exception("No Aurora found!")

if __name__ == "__main__":
  print ("Aurora URL: {}".format(findAuroraURL()))

