'''
A. Desarrollo de una calculadora de promedios escolares en Python utilizando variables, operadores, estructuras de control y funciones básicas.

1. Crear un programa que permita al usuario ingresar nombres de materias y sus calificaciones correspondientes (valores entre 0 y 10).

2. Almacenar las materias y calificaciones en estructuras de datos adecuadas (listas).

3. Calcular y mostrar el promedio general de todas las calificaciones ingresadas.

4. Determinar qué materias están aprobadas y reprobadas según un umbral definido (5.0).

5. Identificar y mostrar la materia con la calificación más alta y la más baja.

6. Permitir al usuario agregar tantas materias como desee, con opción para finalizar la entrada de datos.

7. Mostrar un resumen final con toda la información procesada de forma clara.

8. Utilizar exclusivamente programación estructurada (sin clases ni POO).

9. Implementar al menos 3 funciones diferentes para organizar el código.

10.Incluir validación básica de entradas para evitar errores.
'''


def ingresar_calificaciones():
    """"
        Función para ingresar materias y calificaciones, con validación de entrada.

        Arg: None

        Return: 
            Calificaciones actualizadas con los datos ingresados por el usuario.
            Materias actualizadas con los datos ingresados por el usuario.
    """
    calificaciones = []
    materias = []
    
    i = 0
    while True:
        materia = input(f"Ingrese el nombre de la materia {i+1}  ")
        calificacion = float(input(f"Ingrese la calificación para {materia} (entre 0 y 10): "))
        while True: 
            if calificacion < 0 or calificacion > 10:
                print("La calificación debe estar entre 0 y 10. Intente nuevamente.")
                calificacion = float(input(f"Ingrese la calificación para {materia} (entre 0 y 10): "))
            else:
                break

        if 0 <= calificacion <= 10:
            #calificaciones[i] = calificacion
            calificaciones.append(calificacion)
            materias.append(materia)
            #i = 0 - Materia[0]: Matematicas, Califacion[0]: 6
            #i = 1 - Materia[1]: Ingles, Califacion[1]: 8
            i += 1
        else:
            print("La calificación debe estar entre 0 y 10. Intente nuevamente.")
        
        continuar = input("¿Desea ingresar otra materia? (s/n): ").lower()
        if continuar != 's':
            break
    
    return calificaciones, materias



def calcular_promedio(calificaciones): #Calcular Promedios de las calificaciones
    """
        Función para Calcular el promedio de las calificaciones.

        Arg: Calificaciones: Lista para almacenar las calificaciones.
             
        Return: Promedio de las calificaciones ingresadas por el usuario.
    """
    
    if len(calificaciones) == 0:
        return 0
    
    return sum(calificaciones) / len(calificaciones)



def determinar_estado(calificacion, umbral=5.0):
    """
        Función para determinar el estado de una materia según su calificación.

        Arg: Calificación: Valor numérico de la calificación de una materia.
             
        Return: Estado de la materia (Aprobada, Final o Desaprobada).
    """
    i = 0
    aprobados = []
    desaprobados = []
    while i < len(calificacion):
        
        if calificacion[i] >= umbral:
            aprobados.append(i)
            print("Aprobado")

        else:
            desaprobados.append(i)
            print("Desaprobado")
        i += 1
    return aprobados, desaprobados



def encontrar_extremos(calificaciones): 
    """
        Función para encontrar la calificación máxima y mínima.
        Arg: Calificaciones: Lista para almacenar las calificaciones.
        Return: Tupla con el indice de la calificación máxima y mínima ingresada por el usuario.
    """
    for i in range(len(calificaciones)):
        if i == 0:
            indice_maximo = i
        elif calificaciones[i] > calificaciones[indice_maximo]:
            indice_maximo = i

        if i == 0:
            indice_minimo = i
        elif calificaciones[i] < calificaciones[indice_minimo]:
            indice_minimo = i

    return indice_maximo, indice_minimo


    

def mostrar_resumen(calificaciones, materias) -> None:
    """
        Función para mostrar en consola el resumen de materias calificaciones, y estado.

        Arg: Calificaciones: Lista para almacenar las calificaciones.
             Materias: Lista para almacenar los nombres de las materias.
        Return: None
    """
    umbral = 4.0
    print("\nResumen de Materias y Calificaciones:")
    
    
    aprobados, desaprobados = determinar_estado(calificaciones, umbral)
    
    for i in range(len(materias)):
        print(f"{materias[i]}: {calificaciones[i]}")

    promedio = calcular_promedio(calificaciones)
    print(f"\nPromedio General: {promedio:.2f}")

    print(f"\nMaterias Aprobadas: {len(aprobados)}")
    print(f"\nMaterias Desaprobadas: {len(desaprobados)}")

    indice_maximo, indice_minimo = encontrar_extremos(calificaciones)
    print(f"\nCalificación Máxima: {calificaciones[indice_maximo]} en {materias[indice_maximo]}")
    print(f"\nCalificación Mínima: {calificaciones[indice_minimo]} en {materias[indice_minimo]}")
    
    


def main():
    calificaciones, materias  = ingresar_calificaciones()
    mostrar_resumen(calificaciones, materias)



if __name__ == "__main__":
    main()
    print("Programa finalizado. Gracias por usar la calculadora de promedios escolares.")