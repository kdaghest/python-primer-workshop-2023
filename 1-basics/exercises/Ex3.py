# 3. Write a program that asks the user to enter a sentence and then 
# prints the sentence in reverse order. (string manipulation)

f = input("Enter a sentence: ")

result = ""

for j in f:
    result = j + result

print (result)