import sys, os
from http import Request
import ssdp


def pair_with_aurora():
  """
  Gets a new token from the Aurora and writes it into a aurora.token file.
  For this to work, Aurora has to be set in pairing mode by holding its 
  power button for 5 seconds
  """
  base_url = "".format(ssdp.findAuroraURL(), "/api/beta")
  print ("Found Aurora at {}".format(base_url))  
  try: 
    token = request.post("{}/{}".format(base_url, "new"))
  except:
    print ("Failed to pair :( No token generated.")
    print ("Make sure you pressed the Aurora power button for 5 seconds before running this script.")
    return
  with open("aurora.token", "w") as f:
    f.write(token)
  with open("aurora.url", "w") as f:
    f.write(base_url) 
  print ("Wrote token to aurora.token")

if __name__ == "__main__":
  pair_with_aurora()