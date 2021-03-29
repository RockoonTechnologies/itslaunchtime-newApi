import requests, time

DATEFORMAT = "%m/%d/%Y %H:%M:%S"

miscData = {
    "astronauts": [],
    "iss": {"longitude": 0, "latitude": 0},

}

def backgroundTask(delay):
    global miscData
    while True:
        miscData["astonauts"] = []
        astroData = requests.get('http://api.open-notify.org/astros.json').json()["people"]
        for item in astroData:
            miscData["astonauts"].append(item)

        issData = requests.get("http://api.open-notify.org/iss-now.json").json()["iss_position"]
        miscData["iss"]["longitude"] = issData["longitude"]
        miscData["iss"]["latitude"] = issData["latitude"]

        time.sleep(delay)