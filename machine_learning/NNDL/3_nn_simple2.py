import numpy as np

inputs = 3
outputs = 1
n = 2
x = np.random.randn(n,inputs)
y = np.random.randn(n,outputs)
print("x =",x)
print("y =",y)

hiddens = 4
w1 = np.random.randn(inputs,hiddens)
b1 = np.random.rand(1,hiddens)

w2 = np.random.randn(hiddens, outputs)
b2 = np.random.rand(1,outputs)

# print("w1 =",w1.shape)
# print("b1 =",b1)
# print("w2 =",w2.shape)
# print("b2 =",b2)

def sigmoid(x):
  return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)
  
def think(x,y):
  global w1, w2, b1, b2
  x = np.array([x])
  y = np.array([y])

  o1 = sigmoid(np.dot(x,w1) + b1)     # 1 x 4
  o2 = sigmoid(np.dot(o1,w2) + b2)    # 1 x 1

  delta2 = sigmoid_derivative(o2) * (o2-y)                # 1 x 4
  delta1 = sigmoid_derivative(o1) * np.dot(w2,delta2).T   # 1 x 1

  w1 -= 0.1 * np.dot(x.T,delta1)      # 3 x 4
  w2 -= 0.1 * np.dot(o1.T,delta2)     # 4 x 1
  b1 -= 0.1 * np.sum(delta1)
  b2 -= 0.1 * np.sum(delta2)
  
  return o2 - y 

errList = []
def train(epochs):
  for i in range(epochs):
    tempErrors = []
    for j in range(n):
      err = think( x[j],y[j] )
      tempErrors.append( err )
    
    error = np.mean(np.array(tempErrors)**2)
    errList.append(error)

train(100)



import matplotlib.pyplot as plt

plt.plot(errList)
plt.title("Loss History")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()
