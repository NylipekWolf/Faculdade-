from datetime import date

class Objeto:
    def __init__(self, tipo, data, valor):
        self.tipo = tipo
        self.data = data
        self.valor = valor
        pass

    def criacao():
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
            break

while True:
    print('Bem vindo ao sistema')
    Objeto.criacao()

#isso vai dar trabalhooooooooooooooo
#hot dog completo é melhor

        