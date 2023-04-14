import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([
  [0,0],
  [0,1],
  [1,0],
  [1,1]
])


output = np.array([
  0,
  0,
  0,
  1
])

weights = np.random.rand(2)
bias = np.random.rand()

def step(val):
  if val > 0:
    return 1
  return 0


print(weights)
print(bias,end="\n\n")

weightsList = []
biasList = []

for _ in range(10):
  print("iteration", _+1)
  counter = 0
  for i in range(4):
    actual = output[i]
    sum = inputs[i][0] * weights[0] + inputs[i][1] * weights[1] + bias
    pred = step(sum)
    error = actual - pred

    if error != 0:
      weights[0] += 0.1 * error * inputs[i][0]
      weights[1] += 0.1 * error * inputs[i][1]
      bias += 0.1 * error 
    else:
      counter += 1

    print(actual, pred)
    weightsList.append(  [  weights[0], weights[1]  ]  )
    biasList.append(  bias  )
  if counter == 4:
    print(weights, bias)
    break


for i in range(len(weightsList)):
  weights = weightsList[i]
  bias = biasList[i]
  x_values = np.linspace(0, 1, 100)
  y_values = (-weights[0] * x_values - bias) / weights[1]

  color = "red"
  if i == len(weightsList)-1:color = "blue"
  
  plt.plot(x_values, y_values, linestyle="--", color=color)

plt.scatter(inputs[:,0], inputs[:,1], color="#000000")
plt.show()
