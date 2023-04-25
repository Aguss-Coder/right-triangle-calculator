from oneAngle import calculateOneAngleFromAnother
from twoAngles import calculateBothAngles

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