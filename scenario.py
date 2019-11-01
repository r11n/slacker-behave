class Feature():
    def __init__(self, name):
        self.name = name

class Scenario():
    def __init__(self, name, status, feature, duration):
        self.name = name
        self.feature = Feature(feature)
        self.status = status
        self.duration = duration