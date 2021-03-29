
class Event:
    def __init__(self, name="", des="", net=0, other="", status="", vehicle=None):
        self.name = name
        self.description = des
        self.net = net
        self.other = other
        self.status = status
        self.vehicle = vehicle


class Vehicle:
    def __init__(self, name="", stages=0, fp=False):
        self.name = name
        self.stages = stages
        self.flightProven = fp


class Starship(Vehicle):
    def __init__(self, name="", sn=0, stages=0, fp=False):
        Vehicle.__init__(self, name=name, stages=stages, fp=fp)
        self.sn = sn