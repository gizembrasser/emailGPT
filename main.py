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
