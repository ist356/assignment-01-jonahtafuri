'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''
even_values = []  # Initialize as an empty list
odd_values = []  # Initialize as an empty list
inputted_number = 1 # Initialize as a int value

while inputted_number != 0:
    inputted_number = int(input("Enter a number: "))
    if inputted_number == 0:
        break
    if inputted_number % 2 == 0:  #checks for even values
        even_values.append(inputted_number)  # Append the number to the even list
    else:
        odd_values.append(inputted_number)  # Append the number to the odd list
dictionary = {'odd': odd_values, 'even': even_values}
print(dictionary)
