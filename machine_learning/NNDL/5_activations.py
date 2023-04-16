import os
os.system("cls")
import numpy as np
import matplotlib.pyplot as plt

def Axis_stuff():
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position(('data', 0.0))
  ax.spines['bottom'].set_position(('data', 0.0))
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')

def Linear_activation(size,color):
  # f(x) = x
  # range -inf, inf
  # f'(x) = 1  
  xvalues = np.linspace(-size,size)
  yvalues = xvalues
  plt.plot(xvalues,yvalues, color=color)

def Binary_activation(size,color):
  xvalues = np.linspace(-size,size)
  yvalues = xvalues > 0
  plt.scatter(xvalues,np.array(yvalues), color=color)

def Sigmoid_activation(size,color):
  xvalues = np.linspace(-size,size)
  yvalues = 1 / (1 + np.exp(-xvalues))
  plt.plot(xvalues,np.array(yvalues), color=color)

def Tanh_activation(size,color):
  # f(x) = (2 / (1 + e^-2x)) - 1
  xvalues = np.linspace(-size,size)
  yvalues = (2 / (1 + np.exp(-2 * xvalues))) - 1
  plt.plot(xvalues,np.array(yvalues), color=color)

# Rectified Linear Activation Unit
def ReLU_activation(size, color):
  # f(x) = max(0,x)
  xvalues = np.linspace(-size,size)
  yvalues = np.maximum(0,xvalues)
  plt.plot(xvalues,np.array(yvalues), color=color)

def Leaky_ReLU_activation(size, alpha, color):
  xvalues = np.linspace(-size,size)
  yvalues = np.maximum(alpha*xvalues,xvalues)
  plt.plot(xvalues,np.array(yvalues), color=color)

def ELU_activation(size, alpha, color):
  xvalues = np.linspace(-size,size)
  yvalues = np.maximum(alpha*np.exp(xvalues)-1,xvalues)
  plt.plot(xvalues,np.array(yvalues), color=color)

def Softmax_activation(lst):
  arr = []
  denom = 0
  for el in lst: denom += (np.e ^ el)
  for el in lst: arr.append( np.e^el / denom )
  return arr

def Softplus_activation(lst):
  arr = []
  for x in lst: arr.append( np.log(1+np.e^x ) )
  return arr

axis_stuff()
# Linear_activation(1, color="red")
# Binary_activation(10, color="blue")
# Sigmoid_activation(10, color="magenta")
# Tanh_activation(10, color="purple")
# ReLU_activation(10, color="orange")
# Leaky_ReLU_activation(10, 0.1, color="cyan")
# ELU_activation(5,0.5,color="lime")
plt.show()
