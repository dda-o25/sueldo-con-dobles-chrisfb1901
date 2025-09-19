"""
Christian Alonso Flores Burgos

Fecha
19 de septiembre de 2025

Calcular el sueldo semanal de un empleado considerando que las horas trabajadas por encima de 48 se pagan al doble.

"""


# Declaraciones
horas_normales=48

#Entradas
horas_trabajadas = float(input("Horas trabajadas: "))
tarifa_hora = float(input("Tarifa por hora: "))

# Proceso
if horas_trabajadas > horas_normales:
    horas_extras = horas_trabajadas - horas_normales
    sueldo_extras = horas_extras * tarifa_hora * 2
    sueldo_normal = horas_normales * tarifa_hora
else:
    horas_extras = 0
    sueldo_extras = 0
    sueldo_normal = horas_trabajadas * tarifa_hora

sueldo_total = sueldo_normal + sueldo_extras

# Salidas
print("Horas extras:", horas_extras)
print("Sueldo por horas extras:", sueldo_extras)
print("Sueldo total:", sueldo_total)