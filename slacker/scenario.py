class SFeature():
    def __init__(self, name):
        self.name = name

class SStatus():
    def __init__(self, name):
        self.name = name

class SScenario():
    def __init__(self, name, status, feature, duration):
        self.name = name
        self.feature = SFeature(feature)
        self.status = SStatus(status)
        self.duration = duration
