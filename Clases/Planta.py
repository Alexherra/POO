class planta:
    Hojas = "Hojas verdes"
    Tamaño = "Hojas grandes"
    flores = "Rojo"
    Tflores = "Flores grandes"
    Tipo = "Vascular"
    Especie = "Angiospermas"
    Luz_Del_Sol = True

    def espe(self):
        print ("La especie de la planta es --" + str (self.Especie) + "--")
        print ("Es una planta --" + str (self.Tipo) + "--")

    def carac(self):
        print ("Tiene --" + str(self.Tamaño) + "-- de un color --" + str(self.Hojas) + "--" )
    
    def fl(self):
        print ("Da --" + str (self.Tflores) + "-- de color --" + str (self.flores) + "--")

    def luz(self):
        return self.Luz_Del_Sol

    def lux(self):
        if self.luz() == True:
            print("La planta necesita luz del sol para desarrollarse")
        else:
            print("La planta no necesita luz del sol o necesita muy pocapara desarrollarse")

Azucena=planta()
Azucena.espe()
Azucena.carac()
Azucena.fl()
Azucena.lux()