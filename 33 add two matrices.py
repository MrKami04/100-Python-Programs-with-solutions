# program that addition of the two matrices.
print("😍 ------------------------- 😍")

variable_A = [[1 , 5 , 8],
             [4 , 5, 6],
             [7, 8, 9]]

variable_B = [[3 , 5 , 8],
             [4 , 2, 6],
             [7, 1, 9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(variable_A)):
    for j in range(len(variable_A)):
        result[i][j] = variable_A[i][j] + variable_B[i][j]
        
for r in result:
    print(r)