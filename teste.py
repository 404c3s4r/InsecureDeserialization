import pickle 

'''
class AUTOMOVEL:

    def __init__(self, cor='amarelo', ano=2012):
        self.cor = cor; 
        self.ano = ano; 

    def info(self):
        return f'COR: {self.cor} ANO: {self.ano}' 
    
carro = AUTOMOVEL

carro_jose = carro('vermelho', 2013)

#print(carro_jose.info())

print(pickle.dumps(carro_jose))
'''
lista = ['joao', 'lucas'] 

serialized = pickle.dumps(lista)
print(serialized)