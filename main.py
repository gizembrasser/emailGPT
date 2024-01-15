import numpy as np  

from constants import INPUT_FILE

# Hyperparameters
batch_size = 64 # How many independent sequences will we process in each iteration (parallel)?
block_size = 256 # What is the maximum context length for predictions?
max_iters = 5000 # Max amount of iterations (training steps) the model will go through before training stops
eval_interval = 500 # How often the model's performance is evaluated on a validation set
learning_rate = 3e-4 # Step size/rate at which parameters are updated 
eval_iters = 200 # Number of iterations between each evaluation on the validation set
n_embd = 384 # Dimensionality of embedding layer, corresponds to size of the hidden layers in model
n_head = 6 # Number of attention heads in a multi-head attention mechanism
n_layer = 6 # Number of layers in the model
dropout = 0.2 # Dropout rate

np.random.seed(1337)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Sorted list of all the unique characters in the text
chars = sorted(list(set(text)))
vocab_size = len(chars)

# Create mapping from string to integer (stoi) and integer to string (itos)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s] # Encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # Decoder: take a list of integers, output a string

# Encode the entire text dataset and store it in an array
data = np.array(encode(text), dtype="int64")
n = int(0.9*len(data)) # First 90% will be train, rest val
train_data = data[:n]
val_data = data[n:]
