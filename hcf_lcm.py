a, b = input("enter two numbers (with space in between: ").split()

a = int(a)  # Convert from strings to integers
b = int(b)

if a > b:
    x = a
else:
    x = b

for i in range(1, x):
    if a % i == 0 and b % i==0:
        hcf = i

print ("hcf: ", hcf)

lcm = a*b

for j in range(x, a * b):
    if j % a == 0 and j % b == 0:
        lcm = j
        break       # stop as soon as a match is found

print ("lcm : ", lcm)
