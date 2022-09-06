from datetime import date, datetime
from hashlib import new
from tracemalloc import stop

class Objeto:
    def __init__(self,descricao, tipo, data, valor):
        self.tipo = tipo
        self.data = data
        self.valor = valor
        self.descricao = descricao
        pass

    def criacao():

        descricao = input('Digite a descrição : ')      
        while True:
            tipo = input('Seria uma 1.Despesa ou 2.Receita :')
            if tipo.isnumeric():
                if(tipo.isnumeric() == 1):
                    tipo = 'Despesa'
                elif(tipo.isnumeric() == 2):
                    tipo = 'Receita'
                break
            print('Digitou errado')
        while True:
            data = input('Digite a data da compra :')
            if len(data) == 6:
                data = date(20 +int(data[-2:]), int(data[2:4]), int(data[:2]))
            print(data)
            break
        while True: 
            valor = float(input('Digite o valor :'))
            break
        Objeto = Objeto(descricao=descricao, tipo=tipo, data=data, valor=valor)
        stop    
            

while True:
    print('Bem vindo ao sistema')
    Objeto.criacao()
    print(Objeto)
    



#isso vai dar trabalhooooooooooooooo
#hot dog completo é melhor

        