# there is a package named requests which a package that allow us to connect
# to different third party APIs and download some data that we can incorporate
# in ou programs by making web requests (internet request) using our program
# as if it's a browser itself

import requests  # We need to install it manually with pip install requests
import json
import sys


if len(sys.argv) != 2:
    sys.exit()


response = requests.get("https://itunes.apple.com/search?\
entity=song&limit=25&term=" + sys.argv[1])
# If we want to see all the data brought from the itunes server :
print(json.dumps(response.json(), indent=2))

print("\n ==== formatting the json ==== \n")

new = response.json()
for result in new["results"]:
    print(result["trackName"])
