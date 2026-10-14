pila = []

def apilar(libro):
    pila.append(libro)
    print(f"Libro agregado: {libro}")
    
def desapilar():
    if len(pila) == 0:
        print("La pila está vacía")
    else:
        libro = pila.pop()
        print(f"Libro retirado: {libro}")

def mostrar_pila():
    if not pila:
        print("No hay libros")
    else:
        print("Pila actual:", pila)
        print("Libro en el tope:", pila[-1])

# Solicitar nombres de libros mediante input() (Paso 4)
for i in range(3):
    nombre_libro = input("Ingrese el nombre del libro a apilar: ")
    apilar(nombre_libro)

mostrar_pila()
desapilar()
mostrar_pila()