H = int(input("Digite as horas: "))
M = int(input("Digite os minutos: "))

e1_h = H
e1_m = M

H_1 = int(input("Digite as horas: "))
H_2 = int(input("Digite os minutos: "))

e2_h = H_1
e2_m = H_2

somaHoras: int = e1_h + H_1
somaMinutos: int = e1_m + e2_m

if somaMinutos >= 60:
    somaHoras = somaHoras + 1
    somaMinutos = somaMinutos - 60

    if somaHoras > 0:
        somaHoras = somaHoras - 24

    if somaHoras > 24:
        somaHoras = somaHoras - 24

    if somaHoras < 0:
        somaHoras = somaHoras * -1
        
    somaHoras = somaHoras - 12
    print(f"{somaHoras}:{somaMinutos}")
