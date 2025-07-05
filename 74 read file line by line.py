print("😍 --------------------------------- 😍")  

# method readlines
f = open("textfile.txt","r")

lines = f.readlines()
print(lines)

new_lines = [x.strip() for x in lines]
print(new_lines)


print("😍 --------------------------------- 😍")  

# method comprehension
f = open("textfile.txt","r")
line = [line for line in f]
print(line)

newline = [x.strip() for x in line]
print(newline)
    
