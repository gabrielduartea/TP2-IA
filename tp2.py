import copy



  
  


def verificar(matriz):
  aux=False
  cont=0
  if matriz[0][0]==1:
    cont=cont+1
  if matriz[0][1]==2:
    cont=cont+1
  if matriz[0][2]==3:
    cont=cont+1 
  if matriz[1][0]==4:
    cont=cont+1     
  if matriz[1][1]==5:
    cont=cont+1
  if matriz[1][2]==6:
    cont=cont+1
  if matriz[2][0]==7:
    cont=cont+1
  if matriz[2][1]==8:
    cont=cont+1
  if matriz[2][2]==0:
    cont=cont+1 
  if cont==9:
    aux=True
  return aux         
        
def imprime(matriz): 
  
  print(matriz[0])
  print(matriz[1])
  print(matriz[2],"\n")
  


def busca_gulosa(matriz):
  
  lista=[]
  lista.append(matriz)
  num=0
  parar=False
  while(parar==False):
    no = lista[-1]
     
      
    num=num+1
    imprime (no)
   
    
    
      
    if h1(lista[-1]) == 0:
        
      print("\n** Você chegou a solução!  ***]\n","Número de nós expandidos=",num)
      
      print(lista)
        
      imprime(no)
      parar==True
      break;
    else:
        
      filho = jogar(no,aresta)
        
      a1=filho[0]
       
      for n in filho:
        w=h1(n)
        print(w)
        
          
        if h1(a1)>>w:
            
          lista.append(n)
          a1=w
          
          

            
        
def busca_A(matriz):
  
  lista=[]
  
   
  lista.append(matriz)
  num=0
  parar=False
  while(parar==False):
    no = lista[-1]
     
      
    num=num+1
    imprime (no)
   
    
    
      
    if h2(lista[-1]) == 0:
        
      print("\n** Você chegou a solução!  ***]\n","Número de nós expandidos=",num)
      
      print(lista)
        
      imprime(no)
      parar==True
      break;
    else:
        
      filho = jogar(no,aresta)
        
      a2=filho[0]
       
      for n in filho:
        w=h2(n)
        
        
          
        if h2(a2)+1>>w:
            
          lista.append(n)
          a2=w
        
          
def h1(matriz):

    aux=0
    
    if matriz[0][0]!=1:
      aux=aux+1
    if matriz[0][1]!=2:
      aux=aux+1
    if matriz[0][2]!=3:
      aux=aux+1 
    if matriz[1][0]!=4:
      aux=aux+1     
    if matriz[1][1]!=5:
      aux=aux+1
    if matriz[1][2]!=6:
      aux=aux+1
    if matriz[2][0]!=7:
      aux=aux+1
    if matriz[2][1]!=8:
      aux=aux+1
    if matriz[2][2]!=0:
      aux=aux+1 
    return aux

  
def h2(tab): 
  aux = 0
  for i in range(3):
    for j in range(3):
      if(tab[i][j]==1):
        aux = aux + abs(0-i) + abs(0-j)
      if(tab[i][j]==2):
        aux = aux + abs(0-i) + abs(1-j)
      if(tab[i][j]==3):
        aux = aux + abs(0-i) + abs(2-j)
      if(tab[i][j]==4):
        aux = aux + abs(1-i) + abs(0-j)
      if(tab[i][j]==5):
        aux = aux + abs(1-i) + abs(1-j)
      if(tab[i][j]==6):
        aux = aux + abs(1-i) + abs(2-j)
      if(tab[i][j]==7):
        aux = aux + abs(2-i) + abs(0-j)
      if(tab[i][j]==8):
        aux = aux + abs(2-i) + abs(1-j)
      if(tab[i][j]==0):
        aux = aux + abs(2-i) + abs(2-j)
  return aux




def jogar(matriz,aresta):

    trocas=[]

    if matriz[0][0]==aresta:
    
      aux = copy.deepcopy(matriz) 
      aux[0][0] = aux[1][0]
      aux[1][0] = aresta
    
    
      trocas.append(aux)
   
      aux = copy.deepcopy(matriz) 
      aux[0][0] = aux[0][1]
      aux[0][1] = aresta
    
    
      trocas.append(aux)
 
   
    elif matriz[0][1]==aresta:

      aux = copy.deepcopy(matriz) 
      aux[0][1] = aux[1][1]
      aux[1][1] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[0][1] = aux[0][0]
      aux[0][0] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[0][1] = aux[0][2]
      aux[0][2] = aresta
    
    
      trocas.append(aux)
   
    elif matriz[0][2]==aresta:
 
      aux = copy.deepcopy(matriz) 
      aux[0][2] = aux[1][2]
      aux[1][2] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[0][2] = aux[0][1]
      aux[0][1] = aresta
    
    
      trocas.append(aux)
   
    elif matriz[1][0]==0:
  
      aux = copy.deepcopy(matriz) 
      aux[1][0] = aux[0][0]
      aux[0][0] = aresta
    
    
      trocas.append(aux)
  
      aux = copy.deepcopy(matriz) 
      aux[1][0] = aux[2][0]
      aux[2][0] = aresta
    
    
      trocas.append(aux)
  
      aux = copy.deepcopy(matriz) 
      aux[1][0] = aux[1][1]
      aux[1][1] = aresta
    
    
      trocas.append(aux)
   
   
    elif matriz[1][1]==aresta:
    
      aux = copy.deepcopy(matriz) 
      aux[1][1] =  aux[0][1]
      aux[0][1] = aresta
    
     
      trocas.append(aux)

      aux = copy.deepcopy(matriz) 
      aux[1][1] = aux[1][0]
      aux[1][0] = aresta
    
    
      trocas.append(aux)

      aux = copy.deepcopy(matriz) 
      aux[1][1] = aux[1][2]
      aux[1][2] = aresta
    
    
      trocas.append(aux)
 
      aux = copy.deepcopy(matriz) 
      aux[1][1] = aux[2][1]
      aux[2][1] = aresta
    
    
      trocas.append(aux)
   
   
    elif matriz[1][2]==0:
  
      aux = copy.deepcopy(matriz) 
      aux[1][2] = aux[0][2]
      aux[0][2] = aresta
    
    
      trocas.append(aux)
  
      aux = copy.deepcopy(matriz) 
      aux[1][2] = aux[2][2]
      aux[2][2] = aresta
    
    
      trocas.append(aux)
  
      aux = copy.deepcopy(matriz) 
      aux[1][2] = aux[1][1]
      aux[1][1] = aresta
    
    
      trocas.append(aux)
    
    
    
  
    elif matriz[2][0]==aresta:
    
      aux = copy.deepcopy(matriz) 
      aux[2][0] = aux[1][0]
      aux[1][0] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[2][0] = aux[2][1]
      aux[2][1] = aresta
    
    
      trocas.append(aux)
  
    elif matriz[2][1]==aresta:

      aux = copy.deepcopy(matriz) 
      aux[2][1] = aux[1][1]
      aux[1][1] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[2][1] = aux[2][0]
      aux[2][0] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[2][1] = aux[2][2]
      aux[2][2] = aresta
    
    
      trocas.append(aux)
    
    elif matriz[2][2]==aresta:
    
      aux = copy.deepcopy(matriz) 
      aux[2][2] = aux[1][2]
      aux[1][2] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[2][2] = aux[2][1]
      aux[2][1] = aresta
    
    
      trocas.append(aux)
  
    return trocas

print("Digite a sequencia desejada para iniciar o jogo, o '0' representa a opçao vazia!")

a=int(input("Digite o primeiro numero:"))
b=int(input("Digite o segundo numero:"))
c=int(input("Digite o terceiro numero:"))
d=int(input("Digite o quarto numero:"))
e=int(input("Digite o quinto numero:"))
f=int(input("Digite o sexto numero:"))
g=int(input("Digite o setimo numero:"))
h=int(input("Digite o oitavo numero:"))
i=int(input("Digite o nono numero:"))

matriz=[
    [a,b,c],
    [d,e,f],
    [g,h,i],
  
    
    
]
 
 
 


aresta=0   
    



aresta=0
op = int(input('Informe uma opção de busca:\n1-Busca Gulosa.\n2-Busca A*\n'))
if(op==1):
  busca_gulosa(matriz)
elif(op==2):
  busca_A(matriz)   

