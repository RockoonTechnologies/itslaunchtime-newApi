from flask import Flask, redirect, jsonify, request
import threading
from flask_cors import CORS

from classes import *
import misc

app = Flask(__name__)
CORS(app)

event = Event()
vehicle = Starship()



with open(SAVEFILE, "r") as f:
 data = json.load(f)
 event.fromJson(data["event"])
 vehicle.fromJson(data["vehicle"])


@app.route('/')
def home():
    return redirect("/uptime")

@app.route('/uptime')
def uptime():
    return "up"

@app.route('/canary/stump')
def canaryredirect():
    return redirect("https://d6s79.csb.app/")

@app.route('/internal/edit')
def apiredirect():
    return redirect("https://replit.com/@dwnlnk/api#main.py")

@app.route('/docs')
def docs():
    return redirect("https://itslaunchti.me/api")

@app.route('/internal/temp/videos')
def tempvideos():
    return jsonify({
        "b1": "sTA0GTgFn5E",
        "b2": "qCbgoqMcirI",
        "b3": "tYZaaz8UbRE",
        "b4": "T07AfvJwZ4g",
        "b5": "richjW1jj20"
    })

@app.route('/internal/channels')
def channels():
    return jsonify({
        "ea": "qCbgoqMcirI",
        "nsf": "tYZaaz8UbRE",
        "lp": "sTA0GTgFn5E",
        "jr": "https://www.youtube.com/watch?v=4j0s3X7o3b8"
    })

@app.route("/v1/event")
def events():
    return jsonify(event.jsonify)

@app.route("/v1/vehicle")
def vehicles():
    return jsonify(vehicle.jsonify())

@app.route("/v1/data")
def data():
    return jsonify({
        "status": event.status.value,
        "event": event.jsonify(),
        "vehicle": vehicle.jsonify(),
        "other": event.other
    })

@app.route("/v1/updateVehicle", methods=["POST"])
def updateVec():
    global vehicle
    auth = True
    if auth:
        data = request.json

        keys = data.keys()
        dicT = vehicle.jsonify()
        for item in keys:
            if item in dicT:
                dicT[item] = data[item]

        vehicle.fromJson(dicT)
    save(event.jsonify(), vehicle.jsonify())
    return jsonify({"Result": "success"})

@app.route("/v1/updateEvent", methods=["POST"])
def updateEvent():
    global event
    auth = True
    if auth:
        data = request.json
        keys = data.keys()
        Dict = event.__dict__
        for item in keys:
            if item in Dict:
                if item == "status":
                  event.status.set(data[item])
                elif item == "net":
                  event.net.set(data[item])
                else:
                  Dict[item] = data[item]
    save(event.jsonify(), vehicle.jsonify())
    return jsonify({"Result": "success"})

@app.route("/v1/notif")
def notifData():
    return jsonify(getNotifData())


@app.route("/v1/misc")
def miscData():
    return jsonify(misc.miscData)


if __name__ == '__main__':
    threading.Thread(target=misc.backgroundTask, args=(3,)).start()
    app.run(host="0.0.0.0")
