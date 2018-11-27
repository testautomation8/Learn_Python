class Phone(object):
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def gettype(self):
        return self.name

    def getmodel(self):
        return self.model

    def __str__(self):
        return "This phone is of type %s and model is %s" % (self.name, self.model)