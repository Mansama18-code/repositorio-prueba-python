'''
Enviar por: https://www.onlinegdb.com/ al campus

Práctica Diagnóstica de Programación I:

Crear un programa que permita al usuario ingresar nombres de materias y sus calificaciones correspondientes (valores entre 1 y 10).

¿Qué debe hacer el programa?
Almacenar las materias y calificaciones en estructuras de datos adecuadas (listas sino variables). Permitir al usuario agregar tantas materias como desee, con opción para finalizar la entrada de datos.
Calcular y mostrar el promedio general de todas las calificaciones ingresadas.
Determinar qué materias están aprobadas y desaprobadas según criterios (mayor igual a 6 APD, mayor, igual a 4 final, menor a cuatro desaprobado).
Mostrar un resumen final con toda la información procesada de forma clara.
Utilizar exclusivamente programación estructurada (sin clases ni POO).

Opcional:
Implementar al menos 2 funciones diferentes para organizar el código (Si las manejas).
Incluir validación básica de entradas para evitar errores (Notas deben ser números).
Identificar y mostrar la materia con la calificación más alta y la más baja.

'''


def ingresar_materias(calificaciones, materias, numero_materias):
    i = 0
    while i < numero_materias:
        materia = input(f"Ingrese el nombre de la materia {i+1}  ")
       
        
        calificacion = float(input(f"Ingrese la calificación para {materia} (entre 1 y 10): "))
        if 1 <= calificacion <= 10:
            materias[i] = materia
            calificaciones[i] = calificacion
        else:
            print("La calificación debe estar entre 1 y 10. Intente nuevamente.")
        i += 1
    
    return calificaciones, materias

def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)

    
def mostrar_resumen(calificaciones ,materias):
    print("\nResumen de Materias y Calificaciones:")
    i = 0
    while i < len(materias):
        if calificaciones[i] >= 6:
            estado =  "APD"
        elif calificaciones[i] >= 4:
            estado = "Final"
        else:
            estado = "Desaprobado"
        print(f"{materias[i]}: {calificaciones[i]} - {estado}")
        i += 1
    promedio = calcular_promedio(calificaciones)
    print(f"\nPromedio General: {promedio:.2f}")

def crear_lista_materias(valor_inicial):

    for i in range(5):
        calificaciones = [0] * valor_inicial
        materias = ['0'] * valor_inicial
    return calificaciones, materias

def main():
    numero_materias = int(input("¿Cuántas materias desea ingresar? "))

    calificaciones, materias = crear_lista_materias(numero_materias)
    print(calificaciones, materias)
    calificaciones, materias  = ingresar_materias(calificaciones, materias, numero_materias)

    mostrar_resumen(calificaciones, materias)


main()