
import time
import io
import sys
import os

input = []
uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
  with open(fn) as f:
    content = f.readlines()
    input = [x.strip() for x in content] 
  os.remove(fn)

# Check input layout
for line in input:
  print(line)


upper = {}
rank = {}


def isol_set(p):
    upper[p] = p
    rank[p] = 0

def detect(p):
    if upper[p] != p:
        upper[p] = detect(upper[p])
        
    return upper[p]

def contect(p, q):
    root1 = detect(p)
    root2 = detect(q)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            upper[root2] = root1
        else:
            upper[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def compute_cost(graph):    
    cost = 0
    wt = 0
    for p in graph['vertices']:

        isol_set(p)
    mst = []
    
    edges = graph['edges']
    edges.sort(key=lambda x:x[2])

    for line in edges:
        p, q, weight = line
                
        if detect(p) != detect(q):
            contect(p, q)
            mst.append(line)
            cost = cost + weight
            wt = weight
    
    return cost-wt


array = []
vert = int(input[0].split(' ')[0])
for i in range(vert):
  array.append(i+1)


array1 = []
a =0
for line in input:
  if not (a==0):
    vert1 = int(line.split(' ')[0])''
    vert2 = int(line.split(' ')[1])
    vert3 = int(line.split(' ')[2])
    tupple=(vert1,vert2,vert3)
    array1.append(tupple)
  a = a+1

graph = {
    'vertices': array,
    'edges': array1 
}


#print ANSWER
print("Output is", compute_cost(graph))