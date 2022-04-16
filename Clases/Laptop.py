class laptop:
    pulgadas = "15.6"
    color = "Gris"
    procesador = "Ryzen 7"
    graficas = "GTX 1660"
    RAM = "12"
    Memoria = "1tb"
    Teclado_Retroiluminado = True

    def pantalla(self):
        print ("La laptop tiene una pantalla de --" + str(self.pulgadas) + "'--")
    
    def proceso(self):
        print("Colo de la laptop --" + str(self.color))

    def procs(self):
        print("La laptop cuenta con un procesador --" + str(self.procesador) + "-- una tarjeta grafica --" + str(self.graficas) + "--")
        print("Un disco duro de --" + str(self.Memoria) + "-- y una memoria RAM de --"+ str(self.RAM) + "--")
   
    def teclado(self):
        return self.Teclado_Retroiluminado

    def iluminado(self):
        if self.teclado() == True:
            print("El teclado cuenta con teclado retroiluminado")
        else:
            print("El teclado no cuenta con teclado retroiluminado")

HP = laptop()
HP.pantalla()
HP.proceso()
HP.procs()
HP.iluminado()