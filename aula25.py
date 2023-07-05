"""
Interpolação de básica de strigs
s - string
d e i  - int
f - float
x e X - Hexadecimal (ABCDED0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08x' % (1500, 1500))