from Patrulla import Patrulla 
from Evento import Evento
import requests

class Map:
  patrullas = []
  evento = None

  # Constructor
  def __init__(self):
    num = int(input("Ingrese el numero de patrullas: "))
    arr = []
    for i in range(num):
      patrullaIndex = i + 1
      print("Ingrese la informacion de la patrulla numero: ", patrullaIndex)
      lat = float(input("Ingrese la latitud: "))
      long = float(input("Ingrese la longitud: "))
      radios = float(input("Ingrese los radios: "))
      arr.append(Patrulla(patrullaIndex,lat, long, radios))
    print("Patrullas creadas")
    self.patrullas = arr

  #crea un evento
  def createEvento(self):
    print("ingrese la infomacion del evento")
    lat = float(input("Ingrese la latitud: "))
    long = float(input("Ingrese la longitud: "))
    self.evento = Evento(lat, long)
    
  #
  def getDoubleDistance(self,distancia):
    nums = ['0','1','2','3','4','5','6','7','8','9','.']
    i = 0
    finalNum = ""
    while distancia[i] in nums:
      finalNum += distancia[i]
      i += 1
    return float(finalNum)
  
  def atenciondeEvento(self, patrullaDistancia):
    minimum = self.patrullas[0]
    for key in patrullaDistancia.keys():
      if patrullaDistancia[key] < patrullaDistancia[minimum]:
        minimum = key
    return minimum
 
  def distancePatrullaEvento(self):
    patrullaDistancia = {}
    for i in range(len(self.patrullas)):
      url = f"https://maps.googleapis.com/maps/api/directions/json?origin={self.patrullas[i].lat},{self.patrullas[i].long}&destination={self.evento.lat},{self.evento.long}&key=AIzaSyCu6N_Jv75wSs8TnytapVPub3oSycUPBzk"
      payload={}
      headers = {}
      response = requests.request("GET", url, headers=headers, data=payload)
      locacionEvento = response.json()["routes"][0]["legs"][0]["end_location"]
      carroPolicia = response.json()["routes"][0]["legs"][0]["start_location"]
      distance = response.json()["routes"][0]["legs"][0]["distance"]["text"]
      patrullaDistancia[self.patrullas[i]] = self.getDoubleDistance(distance)
      
    print("La patrulla mas cercana es: ")
    cosa = self.atenciondeEvento(patrullaDistancia).id
    print(cosa)

  def radioDistancia(distancia, r1, r2):
    interseccion = distancia - (r1 + r2)
    return interseccion
  
  def getPerformance():

      return 0

cosa = Map()
cosa.createEvento()
cosa.distancePatrullaEvento()