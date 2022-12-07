from Patrulla import Patrulla 
from Evento import Evento
import requests
from math import sin, cos, sqrt, atan2, radians

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
      coords = input("Ingrese las Coordenadas: ")
      theCoords = self.forCoords(coords)

      radios = float(input("Ingrese el radio: "))
      arr.append(Patrulla(patrullaIndex, float(theCoords[0]), float(theCoords[1]), radios))
    print("Patrullas creadas")
    self.patrullas = arr

  def forCoords(self, coords):
    return coords.split(',')


  #crea un evento
  def createEvento(self):
    print("ingrese la infomacion del evento")
    coords = input("Ingrese las Coordenadas: ")
    theCoords = self.forCoords(coords)

    self.evento = Evento(float(theCoords[0]), float(theCoords[1]))
    
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


  def distPatEvent(self, patrulla, evento):

      url = f"https://maps.googleapis.com/maps/api/directions/json?origin={patrulla.lat},{patrulla.long}&destination={evento.lat},{evento.long}&key=AIzaSyCu6N_Jv75wSs8TnytapVPub3oSycUPBzk"
      payload={}
      headers = {}
      response = requests.request("GET", url, headers=headers, data=payload)
      distance = response.json()["routes"][0]["legs"][0]["distance"]["text"]

      return(float(distance.split(' ')[0]))


  def radioDistancia(self, distancia, r1, r2):
    minDis = r1+r2
    if (minDis <= distancia):
      return 0
    else:
      return minDis-distancia

  
  def getPerformance(self, patrullas, evento):

    dists = []

    patsPerf = []

    perfForAll = []

    for x in patrullas:
        dist = self.distPatEvent(x, evento)

        dists.append(dist)

  
    for x in range(len(patrullas)):
      contTras = 0
      for y in patrullas:
        if patrullas[x] == y: continue

        theDist = self.distanceBetweenPat(evento, y)

        distanceRadio = self.radioDistancia(theDist, patrullas[x].radio, y.radio)

        contTras = contTras + distanceRadio

      patsPerf.append(contTras)


    for x in range(len(patsPerf)):

      perfForAll.append(1/(patsPerf[x]+dists[x]))
      

    return perfForAll



      


  def distanceBetweenPat(self, patrulla1, patrulla2):

    def getDistance(lati1, long1, lati2, long2):# approximate radius of earth in km
      R = 6373.0

      lat1 = radians(lati1)
      lon1 = radians(long1)
      lat2 = radians(lati2)
      lon2 = radians(long2)

      dlon = lon2 - lon1
      dlat = lat2 - lat1

      a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
      c = 2 * atan2(sqrt(a), sqrt(1 - a))

      distance = R * c

      return distance

    distance = getDistance(patrulla1.lat, patrulla1.long, patrulla2.lat, patrulla2.long)

    return(distance)

def getPatrulla(arr):
  theChoosenOne = max(arr)
  anakinSkywalker = arr.index(theChoosenOne)+1

  return (f'The choosen one for this mission is {anakinSkywalker}')




cosa = Map()
cosa.createEvento()

theArray = cosa.getPerformance(cosa.patrullas, cosa.evento)

print(theArray)
print(getPatrulla(theArray))