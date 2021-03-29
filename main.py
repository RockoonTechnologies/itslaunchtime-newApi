from flask import Flask, redirect, jsonify, request
import threading

from classes import *
import misc

app = Flask(__name__)

event = Event()
vehicle = Starship()

@app.route('/')
def home():
    return redirect("https://itslaunchti.me/api")

@app.route('/docs')
def docs():
    return redirect("https://itslaunchti.me/ap")

@app.route("/v1/event")
def events():
    return jsonify(event.__dict__)

@app.route("/v1/vehicle")
def vehicles():
    return jsonify(vehicle.__dict__)

@app.route("/v1/data")
def data():
    return jsonify({
        "status": event.status,
        "event": event.__dict__,
        "vehicle": vehicle.__dict__,
        "other": event.other
    })

@app.route("/v1/updateVehicle", methods=["POST"])
def updateVec():
    auth = True
    if auth:
        data = request.json(force=True)
        keys = data.keys
        Dict = vehicle.__dict__
        for item in keys:
            if item in Dict:
                Dict[item] = data[item]

    return jsonify({"Result": "success"})

@app.route("/v1/updateEvent", methods=["POST"])
def updateEvent():
    auth = True
    if auth:
        data = request.json(force=True)
        keys = data.keys
        Dict = event.__dict__
        for item in keys:
            if item in Dict:
                Dict[item] = data[item]

    return jsonify({"Result": "success"})

@app.route("/v1/misc")
def miscData():
    return jsonify(misc.miscData)


if __name__ == '__main__':
    threading.Thread(target=misc.backgroundTask, args=(3,)).start()
    app.run()