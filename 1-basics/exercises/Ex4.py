# 4. Write a program that creates a list of 5 fruits, asks the user to enter a fruit name, 
# and then checks if the fruit is present in the list. (lists)

f = ["Coconut","Pineapple","Mango","Tangerine","Acai"]

x=input("Enter fruit name: ")

if x in f:
    print("That fruit is in the list.")
else:
    print("That fruit is not in the list.")