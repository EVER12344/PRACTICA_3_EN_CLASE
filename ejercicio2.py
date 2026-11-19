from ejercicio import lista_enlasada


class Nodo:
    def __init__(self, valor):
        self.valor = valor#guarda el valor del nodo
        self.apuntador = None#puntero indica a donde ira
class ListaEnlazada:
    def __init__(self):
        self.cabeza=None #puntero inicializa
        
    def insertar(self, valor):
        nuevo_nodo= Nodo(valor)
        
        if self.cabeza is None:
            self.cabeza= nuevo_nodo
            return
        while  actual.apuntador is not None:
            actual= actual.apuntador
            actual.apuntador= nuevo_nodo        
    def imprimir(self):
        actual= self.cabeza
        while actual is not None:
            print(actual.valor)
            actual= actual.apuntador
        print("fin del nodo")
    print  
 
 #se probara el programa
    mi_lista=lista_enlasada ()
    #creamos la lista vacia
    mi_lista.insertar(10)
    mi_lista.insertar(20)
    mi_lista.insertar(30)
    mi_lista.imprimir()     