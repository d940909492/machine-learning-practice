import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Load MNIST dataset
mnist = fetch_openml('mnist_784')
X, y = mnist.data.astype(float), mnist.target.astype(int)

# Normalize and split data
X /= 255.0
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# One-hot encode labels
encoder = OneHotEncoder(sparse=False)
y_train_encoded = encoder.fit_transform(y_train.reshape(-1, 1))
y_test_encoded = encoder.transform(y_test.reshape(-1, 1))

# Neural Network architecture
input_size = 784
hidden_size = 128
output_size = 10
learning_rate = 0.1

# Initialize weights and biases
np.random.seed(0)
weights_input_hidden = np.random.randn(input_size, hidden_size)
biases_hidden = np.zeros((1, hidden_size))
weights_hidden_output = np.random.randn(hidden_size, output_size)
biases_output = np.zeros((1, output_size))

# Activation function (sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Training loop
epochs = 1000

for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(X_train, weights_input_hidden) + biases_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + biases_output
    output_layer_output = sigmoid(output_layer_input)
    
    # Backpropagation
    output_error = y_train_encoded - output_layer_output
    output_delta = output_error * sigmoid_derivative(output_layer_output)
    
    hidden_layer_error = output_delta.dot(weights_hidden_output.T)
    hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)
    
    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
    biases_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
    weights_input_hidden += X_train.T.dot(hidden_layer_delta) * learning_rate
    biases_hidden += np.sum(hidden_layer_delta, axis=0, keepdims=True) * learning_rate
    
    # Print loss
    if epoch % 100 == 0:
        loss = np.mean(np.square(output_error))
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Testing
hidden_layer_input_test = np.dot(X_test, weights_input_hidden) + biases_hidden
hidden_layer_output_test = sigmoid(hidden_layer_input_test)

output_layer_input_test = np.dot(hidden_layer_output_test, weights_hidden_output) + biases_output
output_layer_output_test = sigmoid(output_layer_input_test)

predicted_labels = np.argmax(output_layer_output_test, axis=1)
accuracy = np.mean(predicted_labels == y_test)
print(f"Test Accuracy: {accuracy:.4f}")
