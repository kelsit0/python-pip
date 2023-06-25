import random
opciones=("piedra","papel","tijeras")
jug=1
comp=1
while comp<=2 and jug<=2:
  print("bienvenido al juego de piedra papel o tijeras")
  jugador=input("1-piedra 2-papel 3-tijeras: ")
  if(jugador not in opciones):
    print("tu opcion no es valida")
  else:
    jugador.lower().strip()
    rival=random.choice(opciones)
    print("rival eligio", rival)
    if(jugador=="piedra" and rival=="tijeras"):
      print("ganaste")
      jug+=1
    elif(jugador=="papel" and rival=="piedra"):
      jug+=1
      print("jug= ", jug)
    elif(jugador=="tijeras" and rival=="papel"):
     print("tu ganas")
     jug+=1
    elif(jugador==rival):
      print("empate")
    else:
      print("perdiste")
      comp+=1
