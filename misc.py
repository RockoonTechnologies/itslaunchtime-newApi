import requests, time

DATEFORMAT = "%m/%d/%Y %H:%M:%S"

miscData = {
    "astronauts": [],
    "iss": {"longitude": 0, "latitude": 0},

}

key = "87a8ae52ae8d7206e9fcb7882879d213"
weatherData = {
    "des": "",
    "iconSymbol": "e",
    "temp": 0,
    "humidity": 0,
    "wind": {
        "speed": 0,
        "direction": 0
    },
    "clouds": 0
}

def backgroundTask(delay):
    global miscData, weatherData
    while True:
        miscData["astonauts"] = []
        astroData = requests.get('http://api.open-notify.org/astros.json').json()["people"]
        for item in astroData:
            miscData["astonauts"].append(item)

        issData = requests.get("http://api.open-notify.org/iss-now.json").json()["iss_position"]
        miscData["iss"]["longitude"] = issData["longitude"]
        miscData["iss"]["latitude"] = issData["latitude"]


        wData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=South Padre Island&appid={key}").json()

        weatherData["des"] = wData["weather"]["description"]
        weatherData["temp"] = round(wData["main"]["temp"] - 273.15,2)
        weatherData["humidity"] = wData["main"]["humidity"]
        weatherData["wind"]["speed"] = wData["wind"]["speed"]
        weatherData["wind"]["direction"] = wData["wind"]["deg"]

        time.sleep(delay)