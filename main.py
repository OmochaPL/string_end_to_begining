''' Please write a program which asks the user for a string.
The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line. '''


input_string = input("Please type in a string: ")
index = 0
while index < len(input_string):
    print(input_string[(len(input_string)-1)- index])
    index += 1
