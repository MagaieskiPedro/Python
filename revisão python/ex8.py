#agora conte contas vezes as letras se repetem
def contar_caracteres(s: str):
    dicio = {}

    # for key,value in enumerate(s):
    #     print(key)
    #     print(value)
    #     dicio[key] = value
    for i in s:
        dicio[i] = dicio.get(i,0) + 1
    print(dicio)
 
    # print(dicio)


palavra = "banana"
contar_caracteres(palavra)
# dic = {}
# cont = 0
# for i in palavra:
#     cont+=1
#     dic.update({cont:i})
# print(dic)