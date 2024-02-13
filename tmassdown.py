import requests
import json
import os

api_key = "AIzaSyDpHgvTrw44E2l8XsqAITILaUWxUfz6szw"
to_grab = int(input("How many to download? "))

index = 0
term = input("What do you want to download? ")

batch_size = 50

try:
    os.mkdir(term)
    os.chdir(term)

except:
    os.chdir(term)

net = ""

for index in range(to_grab // batch_size):
    print("Batch", index + 1, "out of", to_grab // batch_size)

    r = requests.get(
        "https://g.tenor.com/v2/search?q=%s&key=%s&limit=%s&pos=%s" % (term, api_key, to_grab, net)
        )

    if r.status_code == 200:
        gifs = json.loads(r.content)

    else:
        gifs = None

    net = gifs["next"]
        
    for i in gifs["results"]:
        gif = i["media_formats"]["mediumgif"]["url"]

        print("Downloading", gif + " [" + str((gifs["results"].index(i) + 1) + (batch_size * index)) + "/" + str(to_grab) + "]")

        downloaded = False

        with open(i["id"] + ".gif", "wb") as giffile:
            while not downloaded:
                try:
                    req = requests.get(gif)

                    giffile.write(req.content)

                    downloaded = True

                except KeyboardInterrupt:
                    break

                except:
                    print("Error! Whoops! Trying again...")

print("All done!!! :3")

