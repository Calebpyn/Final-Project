from Patrulla import Patrulla 
from Evento import Evento
import requests

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

  def createEvento(self):
    print("ingrese la infomacion del evento")
    lat = float(input("Ingrese la latitud: "))
    long = float(input("Ingrese la longitud: "))
    self.evento = Evento(lat, long)

	def distancePatrullaEvento(self, patrullas, evento):
		patrullaDistancia = {}
		for i in range(len(patrullas)):
			url = f"https://maps.googleapis.com/maps/api/directions/json?origin={patrullas[i].lat},{patrullas[i].long}&destination={evento.lat},{evento.long}&key=AIzaSyCu6N_Jv75wSs8TnytapVPub3oSycUPBzk"
			payload={}
			headers = {}
			response = requests.request("GET", url, headers=headers, data=payload)
			locacionEvento = response.json()["routes"][0]["legs"][0]["end_location"]
			carroPolicia = response.json()["routes"][0]["legs"][0]["start_location"]
			distance = response.json()["routes"][0]["legs"][0]["distance"]["text"]
		patrullaDistancia[patrullas[i]] = distance	
		print(patrullaDistancia)
        
    #INCOMPLETO
  def atenciondeEvento(self, distancias):
    #aqui es donde definimos que patrulla es la que va a atender el evento
    if self.evento == None:
    	print("no se ha creado un evento")
    return 0

    #INCOMPLETO
  def getPerformance():
    return 0

cosa = Map()
cosa.createEvento()
cosa.distancePatrullaEvento(cosa.patrullas, cosa.evento)