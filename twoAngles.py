from main import isUnitDegrees
import math

def calculateBothAngles ():
    sideA = int(input("Ingresa el valor del lado A: "))
    sideB = int(input("Ingresa el valor del lado B: "))
    angle1 = math.atan(sideA / sideB)
    angle2 = math.atan(sideB / sideA)
    isResultInDegrees = isUnitDegrees()
    if isResultInDegrees:
        print(f'los angulos son {angle1} y {angle2} radianes')
    else:
        print(f'los angulos son {math.degrees(angle1)} y {math.degrees(angle2)} grados')