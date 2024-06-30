import random
import math
def MAE(predicts, targets):
  n = len(predicts)
  mae = sum(abs(p-t) for p, t in zip(predicts, targets)) /n
  return mae

def MSE(predicts, targets):
  n = len(predicts)
  mse = sum((p-t)**2 for p, t in zip(predicts, targets)) /n
  return mse

def RMSE(predicts, targets):
  mse = MSE(predicts, targets)
  rmse = math.sqrt(mse)
  return rmse

num_samples = input('Input number of samples ( integer number ) which are generated : ')
if not num_samples.isnumeric():
  print("number of samples must be an integer number")
else:
  num_samples = int(num_samples)
  loss_name = input("Input loss name : ").strip().upper()

  predicts = [random.uniform(0, 10) for i in range(num_samples)]
  targets = [random.uniform(0, 10) for i in range(num_samples)]

  # if loss_name == "mae":
  #   loss = MAE(predicts, targets)
  # elif loss_name == "mse":
  #   loss = MSE(predicts, targets)
  # elif loss_name == "rmse":
  #   loss = RMSE(predicts, targets)
  # else:
  #   print(f'{loss_name} is not supported')
  #   exit()
  
  for i in range(num_samples):
    if loss_name == "mae":
      loss = abs(predicts[i] - targets[i])
    elif loss_name == "mse":
      loss = (predicts[i] - targets[i])**2
    else:
      print(f"{loss_name} is not supported")
      exit()

    total_loss += loss
    print(f'loss name: {loss_name}, sample: {i}: predict = {predicts[i]}, target = {targets[i]}, loss: {loss}')

  if loss_name == "MAE":
      final_loss = MAE(predicts, targets)
  elif loss_name == "MSE":
      final_loss = MSE(predicts, targets)
  print(f'final {loss_name}: {final_loss}')