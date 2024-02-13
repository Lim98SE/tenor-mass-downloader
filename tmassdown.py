import requests
import json
import os

api_key = "YOUR API KEY HERE"
to_grab = int(input("How many to download? "))

index = 0
term = input("What do you want to download? ")

try:
    os.mkdir(term)
    os.chdir(term)

except:
    os.chdir(term)

net = ""

for index in range(to_grab // 50):
    print("Batch", index + 1, "out of", to_grab // 50)

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

        print("Downloading", gif + " [" + str((gifs["results"].index(i) + 1) + (50 * index)) + "/" + str(to_grab) + "]")

        downloaded = False

        with open(i["id"] + ".gif", "wb") as giffile:
            while not downloaded:
                try:
                    req = requests.get(gif)

                    giffile.write(req.content)

                    downloaded = True

                except:
                    print("Error! Whoops! Trying again...")

print("All done!!! :3")

