import os
import numpy as np
os.system("cls")
def sigmoid(s):
  return 1 / (1 + np.exp(-s))
def sigmoid_derivative(o):
  return o * (1-o)

inputs = np.array([[1],[0.7],[1.2]]) 
hidden_neurons = 2
outputs = np.array([[1],[0]])

w1 = np.array([
  [0.5, 1.5, 0.8],
  [0.8, 0.2, -1.6]
])
w2 = np.array([
  [0.9, -1.7, 1.6],
  [1.2, 2.1, -0.2]
])

print("INITIAL WEIGHT 1",w1,sep="\n")
print("INITIAL WEIGHT 2",w2,sep="\n")

# STEP 1
o1 = sigmoid(np.dot( w1, inputs ))
o2 = sigmoid(np.dot( w2,np.vstack(([1],o1)) ))

# STEP 2
delta2 = sigmoid_derivative(o2) * (o2-outputs)
# delta1 = sigmoid_derivative(o1) * np.dot( delta2.T, w2[:,1:] ).T
delta1 = sigmoid_derivative(o1) * np.dot( w2[:,1:], delta2 )

# STEP 3
w1 -= 0.1 * np.dot(delta1, inputs.T)
w2 -= 0.1 * np.dot(delta2, np.vstack(([1],o1)).T)

print("\nUPDATED WEIGHT 1",w1,sep="\n")
print("UPDATED WEIGHT 2",w2,sep="\n")
