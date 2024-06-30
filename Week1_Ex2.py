def is_number(n):
  try:
    float(n)
  except ValueError: # Indentation corrected here
    return False
  return True

def sigmoid(x):
  import math
  return 1/(1 + math.exp(-x))

def relu(x):
  return max(0,x)

def elu(x, alpha = 0.01):
  return x if x > 0 else alpha * (math.exp(x) - 1)

x = input("Input x = ")
if not is_number(x):
  print("x must be a number")
else:
  x = float(x)
  activation_function = input("Input activation Function ( sigmoid | relu | elu ): ")
  if activation_function == "sigmoid":
    print(f'sigmoid: f({x}) = {sigmoid(x)}')
  elif activation_function == "relu": # Corrected the assignment operator from = to ==
    print(f'relu: f({x}) = {relu(x)}')
  elif activation_function == "elu": # Corrected the assignment operator from = to ==
    print(f'elu: f({x}) = {elu(x)}')
  else:
    print(f'{activation_function} is not supported')