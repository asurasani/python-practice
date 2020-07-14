# python-practice
Python Practice
#Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum
# num_1 = 40
# num_2 = 30
# product = num_1 * num_2
# print(product)
# if product > 1000:
#     print(num_1 + num_2)

#Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number
# previous_number = 0
# for i  in range(0, 10, 1):
#     summation = i + previous_number
#     print("Current number is ", i ," Previous number is ", previous_number," Sum: ", summation)
#     previous_number = i

# Question 3: Given a string, display only those characters which are present at an even index number.
# string = "Energy"
# for i in range(0, len(string)-1, 2):
#     print("index:",[i], string[i])

#Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
# string = "energy"
# n = 3
# space = " "
# for i in range(0, len(string)):
#     if i>= n:
#         space = space + string[i]
# print(space)

#Question 5: Given a list of numbers, return True if first and last number of a list is same
# num_list = [10, 20, 30, 40, 50]
# print("Given list is ", num_list)
# if num_list[0] == num_list[-1]:
#     print("True")
# else:
#     print("False")

#Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
# num_list = [10, 20, 33, 46, 55]
# print("Given list is ", num_list)
# for i in num_list:
#     if i//5 == 0:
#         print(i)

#Question 7: Return the total count of sub-string “Emma” appears in the given string
# string = "Emma is good developer. Emma is a writer"
# print(string.count("Emma"))

#Question 8: Print the following pattern
# rows = 6
# for num in range(rows):
#     for i in range(num):
#         print(num, end=" ")
#     print(" ")

#Question 9: Reverse a given number and return true if it is the same as the original number
# rows = 6
# for num in range(rows):
#     for i in range(num):
#         print(num, end=" ")
#     print(" ")

#Question 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list
#create 2 lists
#filter out odd numbers from one list and even numbers from the second
#combine 2 lists into new one
# list_1 = [10, 20, 23, 11, 17]
# list_2 = [13, 43, 24, 36, 12]
# list_3 = []
# for num in list_1:
#     if num % 2 != 0:
#         list_3.append(num)
# for num in list_2:
#     if num % 2 == 0:
#         list_3.append(num)
# print(list_3)

#Question 11: Write a code to extract each digit from an integer, in the reverse order
# int = 1234
# while (int>0):
#     dig = int % 10
#     int = int//10
#     print(dig)

#Question 12: Calculate income tax for the given income by adhering to the below rules
# income = 45000
# if income <= 10000:
#     income_tax = 0
# elif income <= 20000:
#     income_tax = (income - 10000) * 10 / 100
# else:
#     income_tax = 10000 * 10 / 100
#     income_tax += (income - 20000) * 20 / 100
# print(income_tax)

#Question 13: Print multiplication table form 1 to 10
#rows = 10
# for num in range(1,11):
#     for i in range(1,11):
#         print(num * i,end= " ")
#     print(" ")

#Question 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# rows = 5
# for num in range(rows + 1, 0, -1):
#     for i in range(0, num - 1):
#         print("*", end=' ')
#     print(" ")

#Question 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# def exponent(base,exp):
#     base = 2
#     exp = 5
#     answer = base ** exp
#     print(answer)

#Exercise Question 1: Print First 10 natural numbers using while loop
# n = 1
# while (n<=10):
#     print(n)
#     n += 1

#Exercise Question 3: Accept number from user and calculate the sum of all number between 1 and given number
# sum = 0
# n = int(input("Enta a numba: "))
# for i in range(1, n+1):
#     sum += i
# print(sum)
