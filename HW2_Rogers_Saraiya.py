
##Question 1:

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(x)

##Question 2: 


x = [3, 7, 1, 9, 4, 6, 8, 2, 5]

minimum = x[8]

for number in x:
    if minimum > number:
        minimum = number
print(minimum)
    

##Question 3:

i = 0
n = 10

while i <= n:
    print(i)
    i = i + 1


##Question 4:

password = input("what is your password?")
correct_password = 'abc123'

while password != correct_password:
    password = input("that is the incorrect password")

print("Access granted")
