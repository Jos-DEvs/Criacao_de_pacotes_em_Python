import file3_name

v = float(input(' Digite o preço do produto R$: '))

print(f' A metade de {file3_name.moeda(v)} é {file3_name.moeda(file3_name.metade(v))}')
print(f' O dobro de {file3_name.moeda(v)} é {file3_name.moeda(file3_name.dobro(v))}')
print(f' Aumentando o produto de 10%, temos {file3_name.moeda(file3_name.aumentar(v, 10))}')
print(f' Reduzindo o produto de 13%, temos {file3_name.moeda(file3_name.diminuir(v, 13))}')
