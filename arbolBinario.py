# Esta clase es un nodo del arbol, este contendra un dato que es el valor del nodo,
# tambien esta los hijos izquierdo y derecho que inicializan vacios
class NodoArbol:
    def __init__(self,dato):
        self.dato = dato
        self.izq = None
        self.der = None

# En esta parte ya inicia el arbol binario
class ArbolBinario:
    # se inicializa la raiz del arbol como vacio
    def __init__(self):
        self.raiz = None
    # esta funcion es para insertar un valor a los nodos
    def insertar(self,dato):
        if self.raiz is None: #pregunta si el nodo raiz esta vacio
            self.raiz = NodoArbol(dato) #si esta vacio inserta el dato en la raiz
        else:
            self.insertar_recursivo(self.raiz,dato) #si no esta vacio pasa a la funcion de insertar de forma recursiva
    
    def insertar_recursivo(self,nodo,nuevo_dato): 
        if nuevo_dato < nodo.dato: #si el nuevo dato es menor que el dato en este caso de la raiz
            if nodo.izq is None: #pregunta si esta vacio
                nodo.izq = NodoArbol(nuevo_dato) # si se cumple la condición se inserta el dato a la izquierda
            else: 
                self.insertar_recursivo(nodo.izq, nuevo_dato) #si no se llama de nuevo a la funcion y hace el mismo proceso
        else:
            if nodo.der is None: #en este caso si el nuevo dato es mayor al dato puesto
                nodo.der = NodoArbol(nuevo_dato) # se inserta el dato en el nodo derecho
            else:
                self.insertar_recursivo(nodo.der, nuevo_dato) #si no se vuelve a llamar a la funcion y hace el mismo procedimiento
    
    def mostrar_arbol(self):  # Muestra los datos del árbol en orden descendente
        self.mostrar_recursivo(self.raiz,0) #empieza por la raiz que se encuentra en el nivel 0 y se manda a llamar la funcion

    def mostrar_recursivo(self,nodo,nivel): #la funcion va a ir de forma recursiva
        if nodo is not None: #si el nodo no esta vacio
            self.mostrar_recursivo(nodo.der,nivel + 1) #mostar el nodo derecho que se le suma un nivel y ahora es nivel uno
            print("  " * nivel + str(nodo.dato)) 
            self.mostrar_recursivo(nodo.izq, nivel +1) #mostrar el nodo izquierdo que se le suma un nivel y ahora es nivel uno
            #asi va a ir consecutivamente hasta que llegue a un nodo vacio
    def buscar (self,dato):

        #En esta parte es para buscar un valor en el arbol binario
        return self.buscar_recursivo(self.raiz,dato) #te retorna a la funcion de estar buscando con una recursion
    def buscar_recursivo(self,nodo,dato):  #la funcion que busca de manera recursiva
        if nodo is None or nodo.dato == dato: # Si el nodo donde esta es nulo o tiene el dato que estamos buscando...
            return nodo #lo devuelve
        if dato < nodo.dato:
            # Si el dato que estamos buscando es menor que el dato del nodo actual,
        # llamamos a la función recursivamente en el subárbol izquierdo
            return self.buscar_recursivo(nodo.izq,dato)
        # Si el dato que estamos buscando es mayor o igual que el dato del nodo actual,
    # llamamos a la función recursivamente en el subárbol derecho
        return self.buscar_recursivo(nodo.der,dato)
    
    #eliminar
    def eliminar (self,dato):
        self.raiz = self.eliminar_recursivo(self.raiz,dato) #llama a la funcion de eliminar recursivamente
    
    def eliminar_recursivo(self, nodo,dato): 
        if nodo is None:  # Si el nodo actual es nulo, simplemente lo devuelve
            return nodo
        if dato <nodo.dato:
            # Si el dato que estamos eliminando es menor que el dato del nodo actual,
        # llamamos a la función recursivamente en el subárbol izquierdo
            nodo.izq = self.eliminar_recursivo(nodo.izq,dato)
        elif dato > nodo.dato:
            # Si el dato que estamos eliminando es mayor que el dato del nodo actual,
        # llamamos a la función recursivamente en el subárbol derecho
            nodo. der = self.eliminar_recursivo(nodo.der,dato)
        else:
            if( nodo.izq is None): # si no hay nodo izquierdo devuelve el nodo derecho
                return nodo.der
            elif nodo.derecha is None: #si no hay nodo derecho devuelve el nodo izquierdo
                return nodo.izq
            nodo.dato = self.encontrar_minimo(nodo.derecha)
            nodo.derecha = self.eliminar_recursivo(nodo.derecha,nodo.dato)
        return nodo
    def encontrar_minimo(self,nodo):
        actual = nodo
        while(actual.izq is not None):
            actual = actual.izq
        return actual.dato
    
    #realizar un recorrido preorden en el árbol. Un recorrido preorden visita primero el nodo actual, luego el subárbol izquierdo y finalmente el subárbol derecho
    def preOrden(self,nodo,resultado):
        if nodo is not None: #pregunta si el nodo no esta vacio
            resultado.append(nodo.dato) #si no esta vacio guarda el dato del nodo actual en una lista "resultado"
            self.preOrden(nodo.izq,resultado) #hace la misma funcion para el subarbol izquierdo
            self.preOrden(nodo.der,resultado) #hace la misma funcion para el subarbol derecho
    #funcion que hace que devuelva la lista que se creo
    def recorrer_preOrden(self):
        resultado = []
        self.preOrden(self.raiz,resultado)
        return resultado
    
    #recorrido inorden visita el subárbol izquierdo, luego el nodo actual y, finalmente, el subárbol derecho
    def inOrden(self, nodo, resultado):
        if nodo is not None: #pregunta si el nodo no esta vacio
            self.inOrden(nodo.izq, resultado) #pasa primero por el subarbol izquierdo
            resultado.append(nodo.dato) #almacena los datos en una lista llamada "esultado"
            self.inOrden(nodo.der, resultado) #despues pasa por el subarbol derecho

    # Inicia el recorrido inorden y devuelve la lista resultante
    def recorrer_inOrden(self):
        resultado = []
        self.inOrden(self.raiz, resultado)
        return resultado

    #visita primero los nodos hijos (izquierdo y derecho) y luego el nodo actual.
    def postOrden(self, nodo, resultado):
        if nodo is not None: #pregunta si el nodo no esta vacio
            self.postOrden(nodo.izq, resultado) # Recorre el subárbol izquierdo de manera recursiva
            self.postOrden(nodo.der, resultado) # Recorre el subárbol derecho de manera recursiva
            resultado.append(nodo.dato) # Agrega el dato del nodo actual al final de la lista 'resultado'

    # Inicia el recorrido postorden y devuelve la lista resultante
    def recorrer_postOrden(self):
        resultado = []
        self.postOrden(self.raiz, resultado)
        return resultado



#Llamado a la clase
arbol = ArbolBinario()
opcion = "si"
while(opcion == "si"):
    dato_insertar = int(input("INSERTA EL DATO: "))
    arbol.insertar(dato_insertar)
    print("si: continuar insertando elementos")
    print("no: Dejar de insertar")
    opcion = input("Ingresa si o no: ")
    

arbol.mostrar_arbol()

# Realiza el recorrido preorden y muestra los resultados
print("Recorrido Preorden:")
resultado_preorden = arbol.recorrer_preOrden()
print(resultado_preorden)

# Recorre el árbol inorden y muestra el resultado
print("Recorrido Inorden:")
resultado_inorden = arbol.recorrer_inOrden()
print(resultado_inorden)

# Realiza el recorrido postorden y muestra el resultado
resultado_postorden = arbol.recorrer_postOrden()
print("Recorrido Postorden:", resultado_postorden)

# Busca un valor en el árbol y muestra el resultado
dato_buscar = int (input("Que numero quieres buscar: "))
resultado_busqueda = arbol.buscar(dato_buscar)
if resultado_busqueda:
    print(f"El numero {dato_buscar} fue escontrado en el arbol exitosamente")
else:
    print(f"El numero {dato_buscar} no se encontro en arbol")

# Elimina un valor del árbol y muestra el árbol actualizado
dato_eliminar = int (input("Que numero quieres eliminar: "))
arbol.eliminar(dato_eliminar)
print("se elimino")
arbol.mostrar_arbol()

