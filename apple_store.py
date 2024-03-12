print("******************************")
print("***  Hello and welcome to  ***")
print("***    the apple store     ***")
print("******************************")
print()
print("What is your first name: ")
first_name = input()
print("What is your last name: ")
last_name = input()
full_name = first_name + " " + last_name
apples = 20
print()
print("Welcome", full_name, "it is a pleasure to have you at our store today.")
print("Righ now we have", apples, "apples each for $5.\n")
print('How many would you like to buy?')
amount = int(input())
price = amount * 5
apples = apples - amount
print("\nYou bought:", amount," apples\nThe total price would be:", price," dollars\n")
print(apples, "are available after the sale")