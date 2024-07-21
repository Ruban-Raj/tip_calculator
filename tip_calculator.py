#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total = float(input("what was the total bill? "))
tip_per = int(input("what percentage of tip you would like to give?"))
ppl = int(input("How many people to split the bill? "))

#total_int = int(total)
#tip_int = int(tip_per)
#ppl_int = int (ppl)

percentage = total * tip_per / 100
total_spend = total + percentage
#final = round(total_spend / ppl, 2)
#below is also for rounding off the values. The below method is accurate in python by using format instead of round. Round will not specify the second digit if it doesn't have but format does by adding zero
final = "{:.2f}".format(total_spend / ppl)

print(f"Each person should pay: {final}")

