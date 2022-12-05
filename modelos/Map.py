from Patrulla import Patrulla 
from Evento import Evento
class Map:
    patrullas = []
    evento = None

    def __init__(self):
        num = int(input("Ingrese el numero de patrullas: "))
        arr = []
        for i in range(num):
            print("Ingrese la informacion de la patrulla numero: ", i+1)
            lat = float(input("Ingrese la latitud: "))
            long = float(input("Ingrese la longitud: "))
            radios = float(input("Ingrese los radios: "))
            arr.append(Patrulla(lat, long, radios))
        print("Patrullas creadas")
        self.patrullas = arr

    def createEvento(self, evento):
        print("ingrese la infomacion del evento")
        lat = float(input("Ingrese la latitud: "))
        long = float(input("Ingrese la longitud: "))
        self.evento = evento(lat, long)

    #INCOMPLETO
    def distancePatrullaEvento(self, patrulla):

        return 0
        # url = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyCu6N_Jv75wSs8TnytapVPub3oSycUPBzk"
        # payload={}
        # headers = {}
        # response = requests.request("GET", url, headers=headers, data=payload)
        # cosa = response.json()["routes"][0]["legs"][0]["end_location"]
        # cosa2 = response.json()["routes"][0]["legs"][0]["start_location"]
        # print(cosa)
        # print(cosa2)
    
    #INCOMPLETO
    def atenciondeEvento(self):
        #aqui es donde definimos que patrulla es la que va a atender el evento
        if self.evento == None:
            print("no se ha creado un evento")
        return 0
    #INCOMPLETO
    def getPerformance():
        return 0
    
cosa = Map()