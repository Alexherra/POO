class tv:
    pulgas = "32"
    tipo = "Oled"
    resolucion = "3840 x 2160"
    entradas = "2-USB, 3-HDMI"
    Smart_TV = False

    def prenderTV(self):
        print("Encendiendo")
        print("Encendido, verificando estado ...")
    
    def estado(self):
        print ("La resolucion de la pantalla es " + str (self.resolucion))
        print("Entradas detectadas (" + str (self.entradas) + ")" )
        print("Pantalla usada --" + str (self.tipo) + "--")

    def smart(self):
        return self.Smart_TV

    def  conex(self):
        if self.smart() == True:
            print("Conectando a Internet")
        else:
            print("Esta pantalla no es compstible con el uso de internet")


Sony = tv()
Sony.prenderTV()
Sony.estado()
Sony.conex()