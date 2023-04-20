import theano
import theano.tensor as T

# criar as variáveis simbólicas
x = T.scalar('x')
y = T.scalar('y')

# definir a expressão simbólica
z = x**2 + y**2 + 2*x*y

# compilar a expressão para obter uma função
f = theano.function([x, y], z)

# executar a função com alguns valores de entrada
result = f(2, 3)

# imprimir o resultado
print(result)