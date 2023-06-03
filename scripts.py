Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Olá universo')
Olá universo
print('Olá número' % 5+5)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print('Olá número' % 5+5)
TypeError: not all arguments converted during string formatting
print('Olá número', 6+6)
Olá número 12
print('Olá carinha q mora logo ali', 5+5)
Olá carinha q mora logo ali 10
variavel = 5
varivell2 = 5
print (variavel + variavel)
10
print(variavel + variavel2)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(variavel + variavel2)
NameError: name 'variavel2' is not defined. Did you mean: 'variavel'?
clear
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
nome = 'Ícaro Nogueira'
peso = 800.5
idade = 99
print(nome \n peso \n idade)
SyntaxError: unexpected character after line continuation character
print(nome, \n idade, \n peso)
SyntaxError: unexpected character after line continuation character
print(nome, idade, peso)
Ícaro Nogueira 99 800.5
print('Nome: ' + nome, 'Idade: ' + idade, 'Peso: ' + peso)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print('Nome: ' + nome, 'Idade: ' + idade, 'Peso: ' + peso)
TypeError: can only concatenate str (not "int") to str
print('Nome: ', nome, 'Idade: ', idade, 'Peso: ', peso)
Nome:  Ícaro Nogueira Idade:  99 Peso:  800.5