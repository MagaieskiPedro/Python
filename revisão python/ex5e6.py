num = int(input("Digite um numero: "))
for i in range(num+1):
    print(i)
lista = []
num2 = 0
while num2 >= 0:
   num2 = int(input("Digite um numero: "))
   if num2 <0:
       break
   lista.append(num2)
print(sum(lista))
