# Use the following list - [1,11,14,5,8,9]

#Create a list of numbers that are less than ten using l_1 and list comprehension

#Your output should [1,5,8,9]


l_1 = [1,11,14,5,8,9]


a = [numbers for numbers in l_1 if numbers < 10] 

print(a)

