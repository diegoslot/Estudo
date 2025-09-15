variavel=10 #inteiro
variavel2="Teste" #caractere
lista=[1,2,3,4,5,6,7]
print(len(lista))#mede tamanho
media=(10+10)/2
media2=int(media)

if media2>=12:
    print("aprovado")
elif media==10:
    print("Quase")
else:
    print("reprovado")
    
i=0
while i<=10:
    if i==5:
        break
    print(i)
    i+=1
    
print(60*"*")
 
for i in range(1,11,3): #for com range
    print(i)
print(60*"*")

lista=[]
lista2=[1,10,3,5,9,7,8]
lista3=["Maria","Alfredo","Zé","Bruno"]
lista.append(10)#insere um após o outro
lista.insert(0,50)#insere na posição exata
lista.append(90)
lista.insert(6,70)
del lista[0]#remove por posição
lista.remove(90)#remove pelo valor
lista.pop(0)#remove por posição
lista2.sort()#ordena em ordem crescente
lista3.sort()
lista2.reverse()#reverte a lista
print(lista3.index("Bruno"))
print(lista2)
print(lista3)