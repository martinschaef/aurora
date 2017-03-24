import sys, os
import ssdp

from http import Request

from time import sleep

class Aurora(object):

  def __init__(self, token_file_name, fixed_url_string=None):
    if not os.path.isfile(token_file_name):
      raise Exception("token file not found: {}".format(token_file_name))

    with open(token_file_name, 'r') as f:
      token_string=f.read()

    if fixed_url_string==None:
      self.base_url = "{}/api/beta".format(ssdp.findAuroraURL())
    else:
      self.base_url = "{}/api/beta".format(fixed_url_string)
    self.token = token_string
    self.auth_url = "{}/{}".format(self.base_url, token_string)
    self.state = self.get()
    print self.state

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
  sleep(3)
  aurora.turnOn(False)



