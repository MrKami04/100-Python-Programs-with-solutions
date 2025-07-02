# proram that find the transpose of the matrix.
print("😍 ------------------------- 😍")

# method 1   (by for loop)


variable_A = [[3, 5 , 8],
             [4 , 5, 6]]

variable_T = [[0,0],
              [0,0]
              ,[0,0]]

for i in range (len(variable_A)):
    for j in range (len(variable_A[0])):
        variable_T[j][i] = variable_A[i][j]
        
for i in variable_T:
    print(i)
    
    
# method 2            (list comprehension)
print("😍 ------------------------- 😍")

variable_A = [[3, 5 , 8],
             [4 , 5, 6]]
Transpose = [[variable_A[j][i] for j in range (len(variable_A))]  for i in range (len(variable_A[0]))]
for i in Transpose:
    print(i)