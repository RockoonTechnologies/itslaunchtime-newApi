import json
import random
import datetime

SAVEFILE = "savefile.json"
DATEFORMAT = "%m/%d/%Y, %H:%M:%S"
NOTIFUPDATEFUNC = None

notificationData = {}


class callbackVar:
    def __init__(self, initialValue=None, callback="", args=()):
        self.value = initialValue
        self.__callback = callback
        self.__argus = args

    def work(self):
        print(self.__argus)

    def runCallback(self):
        print(self.__argus)
        for item in self.__argus:
            if item == "value":
                self.__argus[self.__argus.index(item)] = self.value

        self.__callback(self.__argus)

    def set(self, newValue):
        self.value = newValue
        print(newValue)
        self.runCallback()


class Event:
    def __init__(self, name="", des="", net=0, other="", status="", vehicle=None):
        self.name = name
        self.description = des
        self.net = callbackVar(net, callback=notifCallback, args=["net", "value"])
        self.other = other
        self.status = callbackVar(status, callback=notifCallback, args=("status", "value"))
        self.vehicle = vehicle

    def jsonify(self):
        status = self.status.value
        net = self.net.value
        data = self.__dict__.copy()
        data["status"] = status
        data["net"] = net
        return data

    def fromJson(self, data):
        status = callbackVar(data["status"], callback=notifCallback, args=["status", "value"])
        net = callbackVar(data["net"], callback=notifCallback, args=["net", "value"])
        self.__dict__ = data
        self.status = status
        self.net = net
        return self


class Vehicle:
    def __init__(self, name="", stages=0, fp=False, engines=[]):
        self.name = name
        self.stages = stages
        self.flightProven = fp
        self.engines = engines

    def jsonify(self):
        data = self.__dict__.copy()

        data["engines"] = []
        for item in self.engines:
            data["engines"].append(item.__dict__)
        return data

    def fromJson(self, data):
        engineDat = data["engines"]
        self.__dict__ = data
        self.engines = []
        for item in engineDat:
            new = Engine()
            new.__dict__ = item
            self.engines.append(new)

        return self


class Starship(Vehicle):
    def __init__(self, name="", sn=0, stages=0, fp=False):
        Vehicle.__init__(self, name=name, stages=stages, fp=fp, engines=[Raptor(), Raptor(), Raptor()])
        self.sn = sn


class Engine():
    def __init__(self, name="", propellents=[], manufacturer="", engineType="liquid", cycle="", thrust=0,
                 thrustUnits="kN", throttleMin=0, throttleMax=100, slIsp=0, vacIsp=0):
        self.name = name
        self.propellents = propellents
        self.manufacturer = manufacturer
        self.engineType = engineType
        self.cycle = cycle
        self.thrust = {"thrust": thrust, "unit": thrustUnits}
        self.throttle = {"max": throttleMax, "min": throttleMin}
        self.isp = {"SL": slIsp, "VAC": vacIsp}


class Raptor(Engine):
    def __init__(self):
        Engine.__init__(self, name="Raptor", propellents=[{"name": "Methane", "type": "Fuel"},
                                                          {"name": "Liquid Oxygen", "type": "Oxidizer"}],
                        manufacturer="SpaceX", cycle="Full-flow staged combustion", engineType="liquid", thrust=2210,
                        throttleMin=40, throttleMax=100, slIsp=330, vacIsp=380)


def notifCallback(data):
    global notificationData
    message = {
        "message": "",
        "checksum": random.randrange(0, 100000),
        "timestamp": datetime.datetime.now().timestamp(),
    }
    if data[0] == "net":
        message["message"] = f"NET has been updated to {data[1]}"
    else:
        message["message"] = f"Status has been updated to {data[1]}"

    notificationData = message
    print("updated notifs")


def getNotifData():
    return notificationData


def save(event, vec):
    data = {
        "event": event,
        "vehicle": vec
    }
    with open(SAVEFILE, "w") as f:
        json.dump(data, f)