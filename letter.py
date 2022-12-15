
class Stroke:
    
    def __init__(self, coeff):
        self.slopeQuadraticCoeff = coeff

class Letter:

    def __init__(self, name):
        self.name = name
        self.strokesBefore = []
        self.strokesMiddle = []
        self.strokesAfter = []

    def getName(self):
        return self.name

    def setStrokes(self, strokes, pos):
        if pos == "before": self.setStrokesBefore(strokes)
        if pos == "middle": self.setStrokesBefore(strokes)
        if pos == "after": self.setStrokesBefore(strokes)

    def setStrokesBefore(self, strokes):
        self.strokesBefore = strokes
    
    def setStrokesMiddle(self, strokes):
        self.strokesMiddle = strokes

    def setStrokesAfter(self, strokes):
        self.strokesAfter = strokes

    def getStrokesBefore(self):
        return self.strokesBefore
    
    def getStrokesMiddle(self):
        return self.strokesMiddle

    def getStrokesAfter(self):
        return self.strokesAfter
