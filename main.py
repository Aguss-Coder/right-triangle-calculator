import math

def angle (ang):
    result = math.pi - (ang + (math.pi / 2))
    return result

def calc (a, b):
    ang1 = math.atan(a / b)
    ang2 = math.atan(b / a)
    return ang1, ang2

def main ():
    ans = input("El triangulo rectangulo tiene un angulo dado? [S/N]: ")
    if ans == 's':
        data = math.radians(int(input("Ingresa el valor del angulo: ")))
        if data >= (math.pi/2):
            return print("El angulo no puede ser mayor o igual a 90 grados o pi radianes"), main()
        else:
            ang = angle(data)
            ans = input("Resultado en [R]adianes o [G]rados?: ")
            if ans == 'r':
                return print(f'el angulo es {ang} radianes')
            else:
                return print(f'el angulo es {math.degrees(ang)} grados')
    else:
        valA = int(input("Ingresa el valor de a: "))
        valB = int(input("Ingresa el valor de b: "))
        angs = calc(valA, valB)
        ans = input("Resultado en [R]adianes o [G]rados?: ")
        if ans == 'r':
            return f'los angulos son {angs[0]} y {angs[1]} radianes'
        else:
            return f'los angulos son {math.degrees(angs[0])} y {math.degrees(angs[1])} grados'

main()
