import math

def calculateOneAngleFromAnother ():
    angleValue = float(input("Ingresa el valor del ángulo en radianes: "))

    if angleValue >= math.pi / 2:
        return print("El ángulo no puede ser mayor o igual a 90 grados o pi / 2 radianes"), calculateOneAngleFromAnother()
    else:
        angle = math.pi - (angleValue + (math.pi / 2))
        isResultInDegrees = isUnitDegrees()
        if isResultInDegrees:
            print(f'el ángulo es {math.trunc(math.degrees(angle))} grados')
        else:
            print(f'el ángulo es {angle} radianes')

def calculateBothAngles ():
    sideA = int(input("Ingresa el valor del lado A: "))
    sideB = int(input("Ingresa el valor del lado B: "))
    angle1 = math.atan(sideA / sideB)
    angle2 = math.atan(sideB / sideA)
    isResultInDegrees = isUnitDegrees()
    if isResultInDegrees:
        print(f'los angulos son {math.degrees(angle1)} y {math.degrees(angle2)} grados')
    else:
        print(f'los angulos son {angle1} y {angle2} radianes')


def isUnitDegrees ():
    unitToPrint = input("Resultado en [R]adianes o [G]rados?: ")
    answer = unitToPrint.lower()
    return answer == 'r'

def main ():
    hasAngle = input("El triángulo rectángulo tiene un ángulo dado? [S/N]: ")
    if hasAngle.lower() == 's':
        calculateOneAngleFromAnother()
    elif hasAngle.lower() == 'n':
        calculateBothAngles()
    else:
        return print('No se reconoce la respuesta.'), main()

main()