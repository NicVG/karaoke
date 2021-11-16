from collections import deque

canciones=dict()
cola=deque()
i=0

lista=open("canciones.txt","r",encoding="UTF-8")

for linea in lista:
    i+=1
    linea_limpia=linea.strip()
    canciones[str(i)]=["( )",linea_limpia]

for k,v in canciones.items():
            print(k+") "+v[0]+" "+v[1])   



while True:
    print("\n")
    usuario=input("Canciones, Cola, Next o numero de cancion\n")
    print("\n")
    
    if usuario.lower()=="canciones":
        for k,v in canciones.items():
            print(k+") "+v[0]+" "+v[1])
            
    elif usuario.lower()=="cola":
        if len(cola)==0:
            print("No hay nada en la cola.\n")
        else:
            j=0
            print("COLA:")        
            for elementos in cola:
                j+=1
                print(str(j)+". "+elementos)
            
    elif usuario in canciones:
        if canciones[usuario][0]!="(X)":
            cola.append(canciones[usuario][1]+" ["+usuario+"]")
            canciones[usuario][0]="(X)"
            for k,v in canciones.items():
                print(k+") "+v[0]+" "+v[1]) 
            print("\n")
            print(canciones[usuario][1]+" ha sido agregada a la cola.\n")
        else:
            for k,v in canciones.items():
                print(k+") "+v[0]+" "+v[1]) 
            print("\n")
            print(canciones[usuario][1]+" ya se cantó una vez.\n")
                
    elif usuario.lower()=="next":
        if len(cola)>0:
            cola.popleft()
            if len(cola)==0:
                print("No hay nada en la cola.\n")
            else:
                j=0
                print("COLA:")
                for elementos in cola:
                    j+=1
                    print(str(j)+". "+elementos)
        else:
            print("No hay nada en la cola.\n")
                
    else:
        print("Input no reconocido, intentelo de nuevo.\n")