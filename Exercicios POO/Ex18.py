class Calendario:
    #construtor
    def __init__(self,dia=1,diferenca=1,mes=1,bissexto=False):
        self.dia = dia
        self.diferenca = diferenca
        if mes>0 and mes<13:
            self.mes = mes
        self.bissexto = bissexto
    #consulta os dias de um mes informando seu numero e se o ano é bissexto
    def ConsultaMes(self,mes=1,bissexto=False):
        if mes>0 and mes<13:
            if mes == 2 and self.bissexto==True:
                return 29
            elif mes == 2 and self.bissexto==False:
                return 28
            else:
                if mes%2==0:
                    return 30
                else:
                    return 31
    #consulta um qual data será informando um dia, mes em que se encontra e quantos dias atras deseja encontrar essa data
    def ConsultaDias(self,dia,diferenca,mes=1):
        tamanhoMes = self.ConsultaMes(mes)
        if dia-diferenca > tamanhoMes:
            mes = mes-1
            if mes <= 0:
                mes = 12 - (mes-1)
            tamanhoMes = self.ConsultaMes(mes)
            return f"A diferença entre os dias é o dia {dia-diferenca} no mes {mes}"
        else:
            return f"A diferença entre os dias é o dia {dia-diferenca} no mes {mes}"
    #consulta os feriados de um mes
    def ConsultaFeriados(self,mes=1):
        if mes == 1:
            return "No dia 1 é ano novo"
        elif mes == 4:
            return f"No dia 21 do mes {mes} é tiradentes"
        elif mes == 5:
            return f"No dia 1 do mes {mes} é dia do trabalhador"
        elif mes == 9:
            return f"No dia 7 do mes {mes} é dia da independencia"
        elif mes == 10:
            return f"No dia 12 do mes {mes} é dia da padroeira"
        elif mes == 11:
            return f"No dia 2 do mes {mes} é dia dos finados,No dia 15 do mes {mes} é proclamação da republica, No dia 20 do mes {mes} é dia da consciencia negra"
        elif mes == 12:
            return f"No dia 25 do mes {mes} é natal"
        