import tensorflow as tf
from tensorflow import keras

# carregar o conjunto de dados MNIST
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# pré-processamento dos dados
x_train = x_train / 255.0
x_test = x_test / 255.0

# definir a arquitetura da rede neural
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# compilar o modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# treinar o modelo
model.fit(x_train, y_train, epochs=5)

# avaliar o modelo com o conjunto de testes
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Acurácia do modelo:', test_acc