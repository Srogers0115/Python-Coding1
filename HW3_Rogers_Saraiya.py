
##Q1

def even_sum(num_list):
    Even_Sum = 0
    for x in range(Number):
        if(num_list[x] % 2 == 0):
            Even_Sum = Even_Sum + num_list[x]
    return Even_Sum

num_list = []
Number = int(input("Please enter the amount of numbers you want in your list: "))
for y in range(1, Number + 1):
    value = int(input("Please enter the value of %d number : " %y))
    num_list.append(value)


Even_Sum = even_sum(num_list)

if Number > 1:
    print("\nThe sum of even numbers in this list =  ", Even_Sum)
else:
    print("0")


##Q2    

num_list = []
numbers = int(input("Please enter the amount of numbers you want in your list: "))
for y in range(1, numbers + 1):
    value = int(input("Please enter the value of %d number : " %y))
    num_list.append(value)

def largest_difference(num_lst):
    if numbers > 2:
        return max(num_lst) - min(num_lst)
    else:
        return 0

print("the largest difference in your list is", largest_difference(num_list))

