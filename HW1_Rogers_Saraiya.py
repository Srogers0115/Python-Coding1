## Question 1 Q1

print("Please input four values to determine the maximum")

## Question 1 Q2

number1 = int(input('enter first integer:  '))
number2 = int(input('enter second integer: '))
number3 = int(input('enter third integer: '))
number4 = int(input('enter fourth integer: '))

maximum = number1

if number2 > maximum:
    maximum = number2

if number3 > maximum:
    maximum = number3

if number4 > maximum:
    maximum = number4

print('The maximum value is', maximum)

## Question1 Q3

print("Please input four values to determine the minimum")

number1 = int(input('enter first integer:  '))
number2 = int(input('enter second integer: '))
number3 = int(input('enter third integer: '))
number4 = int(input('enter fourth integer: '))

minimum = number1

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

if number4 < minimum:
    minimum = number4

print('The minimum value is', minimum)

## Question 1 Q4

print("Please input four values to determine the sum")

number1 = int(input('enter first integer:  '))
number2 = int(input('enter second integer: '))
number3 = int(input('enter third integer: '))
number4 = int(input('enter fourth integer: '))

sum= number1 + number2 + number3 + number4

print('the sum is', sum)

##Question 1 Q5

print("please input four values to determine the range")

number1 = int(input('enter first integer:  '))
number2 = int(input('enter second integer: '))
number3 = int(input('enter third integer: '))
number4 = int(input('enter fourth integer: '))

maximum = number1

if number2 > maximum:
    maximum = number2

if number3 > maximum:
    maximum = number3

if number4 > maximum:
    maximum = number4

minimum = number1

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

if number4 < minimum:
    minimum = number4

range= maximum - minimum

print('the range is ', range)

## Question 2 Q1

hours_worked = int(input('how many hours did you work last week?'))

## Question 2 Q2

pay_rate = float(input('what is your pay rate per hour?'))
                   
## Question 2 Q3- 3.1

if hours_worked <= 45:
    print(f"no overtime; gross pay = ${hours_worked * pay_rate: .2f}")

## Question 2 Q4
    
else:
    print(f"gross pay = ${(45 * pay_rate) + (hours_worked - 45) * pay_rate * 1.5: .2f}")

## Q4.2

overtime_hours = hours_worked- 45

gross_pay = hours_worked

print('your overtime hours is', overtime_hours, 'your gross pay is $', hours_worked)

## Question 3

temperature= float(input('please enter a temperature in celsius'))

fahrenheit = temperature*1.8+32

print('temperature in fahrenheit is', fahrenheit)

##Question 4

age= float(input("to determine eligibility for voting, what is your age?"))

if age > 18:
    print ("eligible for voting")
else:
    print ("not eligible for voting")

##Question 5

units = int(input("how many units did you use?"))

if units <= 100:
    print('no charge')
elif units > 100 and units <= 200:
    print(f" your bill is {(units - 100) * 5}")
else:
    print(f" your bill is {100*5 + (units - 200)*10}")






