''' 
Program To Make:

Asks the user to input a list of integers separated by spaces.
Sorts the list of integers in ascending order.
Removes any duplicate integers from the sorted list.
Prints the final sorted list without duplicates.

Requirement:
Keywords
import, def, return, if, else, for, in, True, while, pass, print, input, break, continue, sum, range, isnumeric, append, clear, os.system

Libraries: Only OS
'''


# My Program

import os
a = input("Give integers separated by spaces\n")
a+=' '

int_list = []
int_gather = ''
ascending_list = []

target = 0
index = 0

for x in a:
	if x == " ":
		if int(int_gather) in int_list:
			int_gather = ''
			continue
		else:
			int_list.append(int(int_gather))
			int_gather = ''
	int_gather +=x

for x in range(len(int_list)):
	ascending_list.append(1)

for i in range(len(int_list)):
	for x in int_list:
		if int_list[target] > x:
			index+=1
		else:
			pass
	ascending_list[index] = int_list[target]
	index = 0
	target+=1

print(f"Your ascending_list without number repetation is\n{ascending_list}\n")
os.system('pause')

os.system('cls')




# ChatGPT's Program
import os

# Function to check if a number is already in the list
def is_in_list(num, int_list):
    for n in int_list:
        if num == n:
            return True
    return False

# Function to remove duplicates from a list while preserving order
def remove_duplicates(int_list):
    unique_list = []
    for num in int_list:
        if not is_in_list(num, unique_list):
            unique_list.append(num)
    return unique_list

# Function to sort a list of integers in ascending order
def sort_list(int_list):
    sorted_list = []
    for num in int_list:
        for i in range(len(sorted_list)):
            if num < sorted_list[i]:
                sorted_list.insert(i, num)
                break
        else:
            sorted_list.append(num)
    return sorted_list

# Input list of integers from user
print("Enter integers separated by spaces:")
input_str = ""
while True:
    input_char = input("Enter an integer or press Enter to finish: ")
    if input_char == "":
        break
    input_str += input_char + " "

input_list = []

int_gather = ''
for x in input_str:
    if x == " ":
        if int(int_gather) in input_list:
            int_gather = ''
            continue
        else:
            input_list.append(int(int_gather))
            int_gather = ''
    else:
        int_gather += x

# Remove duplicates from the input list
input_list = remove_duplicates(input_list)

# Sort the list in ascending order
sorted_list = sort_list(input_list)

# Print the final sorted list without duplicates
print("Sorted list without duplicates:", sorted_list)
os.system('pause')


'''
Overall, What I'd say is that my program, all it seeked is Simplicity and didn't consider other things like Optimization, Code Beauty and so on.
But, Chat GPT's program included everything from beauty to optimization. Logics are hard to make. I am still learning so I'll keep on improving.
'''
