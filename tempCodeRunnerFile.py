#Part1 Write a program that uses nested loops to 
#collect data and calculate the average rainfall 
#over a period of years. The program should 
#first ask for the number of years. 
#The outer loop will iterate once for each year. 
#The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of rainfall,
# and the average rainfall per month for the entire period.

#The first thing I will do is asking user number of years 
# Get the number of years from the user

total_years = int(input("Enter the number of years: "))

# assigning total months and total rainfall
tot_mon = total_years * 12
tot_rainfall = 0.0

# my outer loop for each year
for year in range(total_years):
    print(f"Year {year + 1}:")
    
    # my inner loop for each month
    for month in range(1, 13):
        rainfall = float(input(f"  Enter the inches of rainfall for month {month}: "))
        tot_rainfall += rainfall

# this calculation is to calculare the average rain fall by month
average_rainfall = tot_rainfall / tot_mon

# Display the results
print(f"\nTotal number of months: {tot_mon}")
print(f"Total inches of rainfall: {tot_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")

#Part 2:
#The CSU Global Bookstore has a book club that awards points to its
#students based on the number of books purchased each month.
# the first thing is asking user number of books bought
book_bought = int(input("What is the total number of books you bought this month? "))

# Determine the number of points awarded
if book_bought  == 0:
    point= 0
elif book_bought == 2:
    point = 5
elif book_bought  == 4:
    point = 15
elif book_bought  == 6:
    point = 30
elif book_bought  >= 8:
    point = 60
else:
    point = 0  

# show the points earned
print(f"Points awarded: {point}")