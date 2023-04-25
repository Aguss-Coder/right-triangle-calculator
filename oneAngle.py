import math
from main import isUnitDegrees

def calculateOneAngleFromAnother ():
    angleValue = float(input("Ingresa el valor del ángulo en radianes: "))

    if angleValue >= math.pi / 2:
        return print("El ángulo no puede ser mayor o igual a 90 grados o pi / 2 radianes"), calculateOneAngleFromAnother()
    else:
        angle = math.pi - (angleValue + (math.pi / 2))
        isResultInDegrees = isUnitDegrees()
        if isResultInDegrees:
            print(f'el ángulo es {angle} radianes')
        else:
            print(f'el ángulo es {math.degrees(angle)} grados')