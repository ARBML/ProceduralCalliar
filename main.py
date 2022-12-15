from letter import Stroke, Letter
from json import load
from random import uniform
#import svgwrite

alphabet = {}

def seed():
    global alphabet

    data = load(open('data.json'))
    for i in data:
        letter = Letter(i['letter'])

        for p in i['strokes']:
            lst = []
            for s in i['strokes'][p]:
                lst.append(Stroke(((s['a'][0], s['a'][1]), (s['b'][0], s['b'][1]), (s['c'][0], s['c'][1]))))

            letter.setStrokes(lst, p)

        alphabet[letter.getName()] = letter


seed()

def drawLetter(letter):
    global alphabet
    beforeS = alphabet[letter].getStrokesBefore()[0].slopeQuadraticCoeff

    print(uniform(beforeS[0][0], beforeS[0][1]))
    print(uniform(beforeS[1][0], beforeS[1][1]))
    print(uniform(beforeS[2][0], beforeS[2][1]))

    beforeS2 = alphabet[letter].getStrokesBefore()[1].slopeQuadraticCoeff
    print(uniform(beforeS2[0][0], beforeS2[0][1]))
    print(uniform(beforeS2[1][0], beforeS2[1][1]))
    print(uniform(beforeS2[2][0], beforeS2[2][1]))

drawLetter('b')