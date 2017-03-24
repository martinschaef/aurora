import sys, os
import ssdp

from http import Request

from time import sleep

class Aurora(object):

  def __init__(self, token_file_name):
    if not os.path.isfile(token_file_name):
      raise Exception("token file not found: {}".format(token_file_name))

    with open(token_file_name, 'r') as f:
      token_string=f.read()

    if os.path.isfile("aurora.url"):
      with open("aurora.url", 'r') as f:
        self.base_url=f.read()
    else:
      self.base_url = "{}/api/beta".format(ssdp.findAuroraURL())

    self.token = token_string
    self.auth_url = "{}/{}".format(self.base_url, token_string)

  def __repr__(self):
    return "<Aurora({base_url}, {token})>".format(**self.__dict__)

  def turnOn(self, value=True):
    data = {"on": value}
    self.put("state", data)

  def put(self, endpoint, data):
    request = Request()
    url = "{}/{}".format(self.auth_url, endpoint)
    print url
    request.put(url, data)

  def get(self, endpoint=None):
    request = Request()
    url = self.auth_url
    if endpoint:
      url = "{}/{}".format(self.auth_url, endpoint)
    print url
    return request.get(url)

if __name__ == "__main__":
  print "Some code to talk to an Aurora light. Remember to run pairing.py once to get the aurora.token file."
  aurora = Aurora("aurora.token")
  aurora.turnOn()
  

  data = {
    "command" : "display",
    "version" : "1.0",
    "animType" : "static",
    "animData" : "4 150 1 100 100 0 2 25 -29 240 3 174 -29 120 4 99 13 180",
    "loop" : False
  }

  try:
    aurora.put("write", data)
  except:
    print "failed"
    pass
  sleep(3)
  

  aurora.turnOn(False)



