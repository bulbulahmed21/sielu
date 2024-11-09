import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sielu(x):
    # Define the SiELU activation function
    term = 2 * math.sqrt(2 / math.pi) * (x + 0.044715 * x**3)
    return 0.5 * x * (2 * sigmoid(term))
