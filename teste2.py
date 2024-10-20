import pickle 

"""
string_bytes = b'\x80\x04\x95<\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tAUTOMOVEL\x94\x93\x94)\x81\x94}\x94(\x8c\x03cor\x94\x8c\x08vermelho\x94\x8c\x03ano\x94M\xdd\x07ub.'
print(string_bytes)

'O PICKLE ARMAZENA INFORMAÇÕES DO AUTOMOVEL E NA HORA DE DESSERIALIZAR ELE PRECISA ENCONTRAR O MODULO'
''' Can't get attribute 'AUTOMOVEL' on <module '__main__' from '/opt/InsecureDeserialization/teste2.py'>'''
print(pickle.loads(string_bytes))


"""

'''O que podemos fazer ? Desserializar algo que não seja um objeto '''
string_bytes = b'\x80\x04\x95\x14\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x04joao\x94\x8c\x05lucas\x94e.'

deserialized = pickle.loads(string_bytes)
print(deserialized)