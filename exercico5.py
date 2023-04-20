import arrow

# criar objetos Arrow para as datas desejadas
data1 = arrow.get('2022-01-01')
data2 = arrow.get('2022-12-31')

# calcular a diferença entre as datas em dias
diferenca = (data2 - data1).days

# exibir a diferença em dias
print('A diferença entre as datas é de', diferenca, 'dias')
