# program that multiply two matrices.
print("😍 ------------------------- 😍")


variable_A = [[1 , 5 , 8],
             [4 , 5, 6],
             [7, 8, 9]]

variable_B = [[3 , 5 , 8,9],
             [4 , 2, 6,3],
             [7, 1, 9,2]]

result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for i in range(len(variable_A)):
    for j in range(len(variable_B[0])):
        for k in range(len(variable_B)):
            result[i][j] += variable_A[i][k] * variable_B[k][j]
            
for i in result:
    print(i) 