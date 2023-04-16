import numpy as np

ANDweights = np.array([[1,1]]) # 1 x 2
print(ANDweights.shape)
ANDbias = -1.5

ORweights = np.array([[1,1]])
ORbias = -0.5

NOTweights = np.array([[-1]])
NOTbias = 0.5

inputs = np.array([
  [[0,0]],
  [[0,1]],
  [[1,0]],
  [[1,1]]
])

def step(val):
  if val > 0:return 1
  return 0

result = np.array([])
print("AND","OR","NOT","AND", sep="\t")
for row in inputs: 
  # row = 1 x 2, weights = 2 x 1, result = 1 x 1
  and1 = step( np.dot(row, ANDweights.T) + ANDbias )
  or1 = step( np.dot(row, ORweights.T) + ORbias )
  not1 = step( np.dot(and1, NOTweights.T) + NOTbias )
  
  and2 = step( np.dot( np.array([not1, or1]), ANDweights.T ) + ANDbias ) # result
  print(and1, or1, not1, and2, sep="\t")
  result = np.append(result,and2)
  
print(result)
