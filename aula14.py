a = 'AAAAAAA'
b = 'BBBBBBBBB'
c = 1.1
string = 'primeira={nome2} segunda={nome1} terceira={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, # {nome1}
    nome2=b, # {nome2}
    nome3=c  # {nome3}
)

print(formato)
