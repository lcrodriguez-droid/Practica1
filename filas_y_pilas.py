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