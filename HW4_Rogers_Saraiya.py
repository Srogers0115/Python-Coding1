
##HW Q1 Palindrome Check

String = input("Please enter a string")

Reverse_string = ""

for i in String:
    Reverse_string = i + Reverse_string
    print("Reversed string is ", Reverse_string)

if String == Reverse_string:
    print("The string is a palindrome")
else:
    print("the string is not a palindrome")

#HW Q2 Restaurant Menu -

menu = { 'burger': 10.99, 'fries': 3.99, 'salad': 7.99 ,'milkshake': 5.99}

for x in menu:
    print(f'{x}: {menu[x]}')

order = input("What would you like to order?")

if order in menu:
    print(f" The price of {order} is ${menu[order]:.2f}.")
else:
    print(f"The {order} is not on the menu")

        
    
    

