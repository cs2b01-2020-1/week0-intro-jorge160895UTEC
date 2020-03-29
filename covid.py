from io import open

def texto(nombreArchivo):
  arch = open(nombreArchivo+".txt","r")
  Ltext = arch.readlines()
  Ltext.pop(0)
  text = "".join(Ltext)
  text = text.replace('\n','')
  arch.close()
  return text

def compara(t1, t2):
  s1 = len(t1)
  s2 = len(t2)
  total = max(s1,s2)
  cont = 0
  for i in range(min(s1,s2)):
    if(t1[i]==t2[i]):
      cont = cont+1

  return round(cont*100/total,1)


#Principal:

nombreGen=["AY274119",
           "AY278488.2",
           "MN908947",
           "MN988668",
           "MN988669"]

gen = [texto(nombreGen[0]),
       texto(nombreGen[1]),
       texto(nombreGen[2]),
       texto(nombreGen[3]),
       texto(nombreGen[4])]

matriz=[]

for i in range(len(gen)):
  matriz.append([0]*len(gen))

for i in range(len(gen)):
  for j in range(len(gen)):
    if i==j:
      matriz[i][j] = 100.0
    else:
      matriz[i][j] = compara(gen[i],gen[j])

#Imprimir

print(end='            ')
for i in range(len(gen)):
  print(nombreGen[i], end='   ')
print()

for i in range(len(gen)):
  print(nombreGen[i], end='      ')
  for j in range(len(gen)):
    print(matriz[i][j], end='       ')
  print()
