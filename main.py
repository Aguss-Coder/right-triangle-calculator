import math

def calculateAngle (angle):
    result = math.pi - (angle + (math.pi / 2))
    return result

def calculateAngles (a, b):
    angle1 = math.atan(a / b)
    angle2 = math.atan(b / a)
    return angle1, angle2

def main ():
    hasAngle = input("El triángulo rectángulo tiene un ángulo dado? [S/N]: ")
    if hasAngle.lower() == 's':
        angleValue = int(input("Ingresa el valor del ángulo en radianes: "))
        angleValueInRadians = math.radians(angleValue)
        if angleValueInRadians >= math.pi / 2:
            return print("El ángulo no puede ser mayor o igual a 90 grados o pi radianes"), main()
        else:
            angle = calculateAngle(angleValue)
            unitToPrint = input("Resultado en [R]adianes o [G]rados?: ")
            if unitToPrint.lower() == 'r':
                print(f'el ángulo es {angle} radianes')
            else:
                print(f'el ángulo es {math.degrees(angle)} grados')
    else:
        sideA = int(input("Ingresa el valor del lado A: "))
        sideB = int(input("Ingresa el valor del lado B: "))
        angle1, angle2 = calculateAngles(sideA, sideB)
        unitToPrint = input("Resultado en [R]adianes o [G]rados?: ")
        if unitToPrint.lower() == 'r':
            print(f'los angulos son {angle1} y {angle2} radianes')
        else:
            print(f'los angulos son {math.degrees(angle1)} y {math.degrees(angle2)} grados')

main()
