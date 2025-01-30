i = 0
media = 0
for i in range(5):
    media += float(input("Digite uma nota: "))
media = media/5
print(media)
if media >=5:
    print("Aprovado")
elif media>=2.5 and media<=5:
    print("Recuperacao")
else:
    print("Reprovado")