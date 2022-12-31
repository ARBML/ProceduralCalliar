from letter import AtomicStroke, Stroke, Letter
from json import load
from random import uniform
import svgwrite
import matplotlib.pyplot as plt

alphabet = {}
strokes = {}


def seedAtomicStrokes():
    global strokes

    data = load(open('data/atomicStrokes.json'))
    for i in data:
        stroke = Stroke(i['atomicStroke'])

        lst = []
        for s in i['strokes']:
            lst.append(AtomicStroke(((s['a'][0], s['a'][1]), (s['b'][0], s['b'][1]), (s['c'][0], s['c'][1])), s['reflector']))

        stroke.atomicStrokes = lst
        strokes[stroke.name] = stroke


def seedLetters():
    global alphabet

    data = load(open('data/letters.json'))
    for i in data:
        alphabet[i['name']] = Letter(i['name'], i["atomicStrokes"])


def seed():
    seedAtomicStrokes()
    seedLetters()


def generateSkeleton(letter):
    global alphabet
    global strokes

    letterStrokes = alphabet[letter].strokes

    data = []
    for i in letterStrokes:
        for j in strokes[i].atomicStrokes:
            data.append((uniform(j.slopeQuadraticCoeff[0][0], j.slopeQuadraticCoeff[0][1]), uniform(j.slopeQuadraticCoeff[1][0], j.slopeQuadraticCoeff[1][1]), uniform(j.slopeQuadraticCoeff[2][0], j.slopeQuadraticCoeff[2][1])))

    return data


def generateLetter(letter):
    return generateSkeleton(letter)


def sample(data, sampleRate = 0.01):
    lst = []
    i = 0
    while i < 1:
        lst.append((i, (data[0]*i*i+data[1]*i+data[2])))
        i += sampleRate

    return lst

def draw(data):
    x = []
    y = []
    aa = 0
    for i in data:
        points = sample(i)
        m = 0
        if (len(y) != 0):
            m = y[-1]
        
        x += list(map(lambda a: a[0] - aa, points))
        y += list(map(lambda a: a[1], points))
        aa += 1
        print("------------------")
        print(x)
        print(y)

    plt.plot(x, y)
    plt.savefig(f"a.png")
        
        # polyLine = svgwrite.shapes.Polyline()
        # polyLine.points = points
        # polyLine.translate(100, 100)
        # # reflect along 100, 100
        # dwg = svgwrite.Drawing(f'{i}.svg')
        # dwg.add(polyLine)
        # dwg.save()

seed()
draw(generateLetter('A'))