import os
import numpy as np
import warnings
warnings.filterwarnings('ignore')
os.system("cls")
class Colors:
  # https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
  black = "\033[1;30m"
  red = "\033[1;31m"
  green = "\033[1;32m"
  yellow = "\033[1;33m"
  blue = "\033[1;34m"
  magenta = "\033[1;35m"
  cyan = "\033[1;36m"
  white = "\033[1;37m"
  default = "\033[1;39m"
  reset = "\033[1;0m"
class NeuralNetwork:
  def __init__(self,input_size=0,hidden_size=0,output_size=0,learning_rate=0.1):
    self.learning_rate = learning_rate
    # WEIGHTS INPUT 2 HIDDEN
    self.h_weights = np.random.randn(input_size,hidden_size)
    self.h_bias = np.array([np.random.randn(hidden_size)])
    
    # WEIGHTS HIDDEN 2 OUTPUT
    self.o_weights = np.random.randn(hidden_size, output_size)
    self.o_bias =  np.array([np.random.randn(output_size)])

  def __sigmoid__(self,x):
    return (1/(1+np.exp(-x)))
  def __sigmoid_derivative__(self,x):
    return (x * (1-x))

  def forward(self,x):
    # print(self.h_weights.T.shape, x.T.shape, " + ", self.h_bias.T.shape)
    self.o1 = self.__sigmoid__(np.dot( self.h_weights.T, x.T )  + self.h_bias.T )

    # print(self.o_weights.T.shape, self.o1.shape, " + ", self.o_bias.T.shape)
    self.o2 = self.__sigmoid__(np.dot( self.o_weights.T, self.o1 ) + self.o_bias.T ) 

  def backward(self, x, y):
    # PREVIOUS MLP.pdf METHOD
    self.delta2 = self.__sigmoid_derivative__(self.o2.T) * (self.o2.T-y)
    self.delta1 = self.__sigmoid_derivative__(self.o1) * np.dot( self.delta2, self.o_weights[:,:].T ).T
    self.h_weights -= self.learning_rate * np.dot(self.delta1, x).T
    self.o_weights -= self.learning_rate * np.dot(self.delta2.T, self.o1.T).T
    err = np.sum(y - self.o2.T)
    
    # SIR'S METHOD
    # err = np.sum(y - self.o2.T)
    # self.delta2 = self.__sigmoid_derivative__(self.o2)
    # print(self.delta2.T.shape, self.o_weights.T.shape)
    # self.h_error = np.dot(self.delta2.T,self.o_weights.T)
    # print(self.h_error.shape, self.delta1.shape)
    # self.h_delta = self.h_error * self.__sigmoid_derivative__(self.delta1)

    return err

  def train(self, x, y, e):
    for i in range(e):
      print(Colors.red,"#ITERATION  ",i+1,Colors.reset,sep="")
      self.forward(x)
      err = self.backward(x,y)
      # print(Colors.magenta+"WEIGHT 1"+Colors.reset,self.h_weights,sep="\n")
      # print(Colors.magenta+"WEIGHT 2"+Colors.reset,self.o_weights,sep="\n")
      print(Colors.yellow+"\tError =", err, Colors.reset)

input_size = 4
output_size = 2
nn = NeuralNetwork(input_size=input_size, hidden_size=5, output_size=output_size, learning_rate=0.1)
x = np.random.randn(100,input_size)
y = np.random.randn(100,output_size)
print(x.tolist())
nn.train(x,y,100)
# nn.forward(x)
# nn.backward(x,y)
