#Lab 7

#Nested lists. Nested lists are a very useful data collection: many
#database formats use nested lists for data storage and exchange (spreadsheets
#and tabular data), science and math use matrices and multidimensional arrays,
#and graphics and video use multidimensional vectors. You already saw some
#examples of nested lists in Problem 1. Let’s practice more:

# 1)Now write your own code to calculate matrix multiplication by scalar:
scalar = 3

A= [[1,0,0],[0,1,0],[0,0,1]]

D = []

for i in range(len(A)) :

    D.append([])

    for j in range(len(A[i])) :

           D[i].append ( A[i][j] *scalar)

print (D)
