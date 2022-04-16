class carro:
    color = "Negro"
    modelo = "Civic"
    año = "2022"
    cilindrios = "4 cilindros"
    velocidades = "6 velocidades"
    transmisión = "Manual"
    alarma = True
    encendido = False

    def model(self):
        print ("Modelo del carro y año --" + str (self.modelo) + "-- --" + str (self.año) + "-- en color " + str (self.color))

    def prendercarro(self):
        print("El veiculo esta encendido")
    
    def carac(self):
        print("El auto tiene transmision --" + str (self.transmisión) + "-- con --" + str (self.velocidades) + "--")
    
    def VelocidadMaxima(self):
        print("La velocidad maxima es 240km x hora")
    
    def inicio(self):
        return self.encendido
    
    def alarm(self):
        if self.inicio() == False:
            print ("La arama esta activa")
        else:
            print ("La alarma esta desactivada")

auto = carro()
auto.model()
auto.prendercarro()
auto.carac()
auto.VelocidadMaxima()
auto.alarm()
