

def ingresar():
 agenda=open("agenda.txt","a")
 print("Digite la información del beneficiario a agregar:")
 for i in range(3):
   x=input()
   agenda.write(x)
   agenda.write('\n')
   #x.append(j)
 if i==2:
   print("El beneficiario ha sido agregado")
 return x

def show():
 x=[]  
 print("Listado de beneficiarios")
 agenda=open("agenda.txt","r")
 for i in agenda:
     x.append(i)
 for i in range(len(x)):
    x[i]=x[i].rstrip()
    x[i]
    print(x[i])
    

def letras():
  x=[] 
  print("Digite la letra por la que empiezan los beneficiarios:")
  agenda=open("agenda.txt","r")
  l=(input())
  for i in agenda:
     i=i.rstrip()
     x.append(i)
  for j in range(len(x)):
      if l in x[j]:
         print("Listado filtrado de beneficiarios: ")
         print(x[j])
         print(x[j+1])
         print(x[j+2])

def nombrecompleto():
  x=[]
  print("Digite el nombre y apellido del beneficiario a buscar:")
  agenda=open("agenda.txt","r")
  l=(input())
  for i in agenda:
     i=i.rstrip()
     x.append(i)
  for i in range(len(x)):
      x[i]  
      if(l==x[i]):
       print("Listado filtrado de beneficiarios:")
       print(x[i])
       print(x[i+1])
       print(x[i+2])  

def eliminar():
  x=[]
  print("Digite la cedula del beneficiario a borrar:")
  agenda=open("agenda.txt","r")
  #x=agenda.readlines() 
  l=(input())
  for i in agenda:
     i=i.rstrip()
     x.append(i)
  for i in range(len(x)):
      x[i]
      if(l==x[i]):
         del x[i]
         del x[i-1]
         del x[i-1]
         agenda=open("agenda.txt","w")
         for i in x:
           i=i.rstrip()
           agenda.write(i+'\n')
           
         break
       
        
  print("El usuario ha sido eliminado del listado") 



i=True

while i==True :
  print("Menu Principal")
  print("1. Ver listado")
  print("2. Ver listado filtrado")
  print("3. Agregar beneficiario")
  print("4. Buscar beneficiario")
  print("5. Borrar beneficiario")
  print("6. Salir")
  x=int(input())
  if x==1:
     imprimir=show()
  if x==2:
     letra=letras()
  if x==3:
    ingresardato=ingresar()   
  if x==4:
    seleccion=nombrecompleto()
  if x==5:
    borrar=eliminar()
  if x==6:
    print("Hasta pronto")
    break