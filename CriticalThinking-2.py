
#Part 1: Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.

#first I assigned values and made simple calculations for all the items I want to be calculated
#the sub_total is where user will enter the charge for the food with out any service or tax charges
sub_total = float(input('What is the charge for the food: '))
sales_tax = sub_total * float(0.07)
total_bill = sub_total + sales_tax
total_tip = total_bill * float(0.18)
grand_total = total_bill + total_tip

#the below statements will print a reciept like values
print(f'Sub Total: {sub_total}')
print(f'Sales Tax (7%): {sales_tax}')
print(f'Total Bill: {total_bill}')
print(f'Total Tip (18%): {total_tip}')
print(f'Grand Total: {grand_total}')

#Part 2:
#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
#If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
#Write a Python program to solve the general version of the above problem. 
#Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
#Your program should output what the time will be on a 24-hour clock when the alarm goes off.

#the first thing is to ask user to enter current time using 24 hour clock.
current_time = int(input("Enter the current time using the 24 hour clock:"))

#then ask them what the wait time is from now
alarm_wait = int(input("In how many hours do you want the alarm to start:"))

#here I added both the current time and alarm wait time and used modulo to find the remainder of 24 which is the time the alarm should start
alarm_time = (current_time + alarm_wait)%24
print(f"The alary will start at:{alarm_time}")
