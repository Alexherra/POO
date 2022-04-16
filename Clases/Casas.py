class casa:
    pintura = "Amarillo"
    Pisos = 2
    largo_casa = 10
    ancho_casa = 15
    ventanas = 6
    puertas = 4

    def metro(self):
        self.cuadrado = self.largo_casa * self.ancho_casa
        print("Los metros cuadrados de la casa son --" + str(self.cuadrado) + "--")
    
    def piso(self):
        print("La casa cuenta con --" + str(self.Pisos) + "-- pisos y cuenta con pintura color --" + str(self.pintura) + "--")

    def ven(self):
        print("La casa cuenta con --" + str(self.ventanas) + "-- ventanas")
        print("La casa cuenta con --" + str(self.puertas) + "-- puertas")

cas = casa()
cas.metro()
cas.piso()
cas.ven()