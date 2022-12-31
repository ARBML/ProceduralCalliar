
class AtomicStroke:
    
    def __init__(self, coeff = None, reflector = None):
        self.slopeQuadraticCoeff = coeff
        self.reflector = reflector

class Stroke:

    def __init__(self, name, atomicStrokes = None):
        self.name = name
        self.atomicStrokes = atomicStrokes

class Letter:
    def __init__(self, name, strokes):
        self.name = name
        self.strokes = strokes