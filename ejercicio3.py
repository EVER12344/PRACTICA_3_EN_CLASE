class nodo:
    def __init__(self,dato):
        self.dato = dato#guardado el valor del nodo
        self.siguiente= None #apunta al siguiente
        self.anterior = None #apunta al anterior
        
        
class lista_doble:
    def __init__(self):
        self.inicio = None #puntero inicializa
        self.final = None #puntero finaliza
    
    #agregar un nuebvo nodo
    def insertar(self,dato):
        nuevo=nodo(dato) #crear un nuevo nodo en la lista
        if self.inicio is None: # el nodo esta vacio
            self.inicio= nuevo #opcion true (el inicio toma el valor del nuevo nodo)
            self.final= nuevo #como el finsl  toma el valor del nuevpo nodo
        else:
            nuevo.siguiente= self.inicio #el nuevo nodo apunta al que era primero
            self.inicio.anterior= nuevo #el viejo primer nodo apunta al nuevo nodo
            self.inicio= nuevo  #actualizamos datos

    def insertar_final(self,dato):
        nuevo=nodo(dato)
        if self.final is None:
            self.inicio= nuevo
            self.final= nuevo
        else:
            self.final.siguiente= nuevo
            nuevo.anterior= self.final
            self.final= nuevo

    def imprimir(self):
        actual= self.inicio
        while actual is not None:
            print(actual.dato)
            actual= actual.siguiente
        print("fin de la lista")

#imprimir la lista
tren_nodo= lista_doble()
tren_nodo.insertar(10)
tren_nodo.insertar_final(20)
tren_nodo.insertar(30)
tren_nodo.imprimir()

        
   