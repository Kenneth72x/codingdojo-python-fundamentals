#Countdown: Create a function that accepts a number as an input. Return a new list that counts down one by one, 
#from the number (as the 0th element) down to 0 (as the last element.)
#Example: countdown(5) should return [5,4,3,2,1,0]
def countdown(num):
    nums_list = []
    for val in range(num,-1,-1):
        nums_list.append(val)
    return nums_list

print(countdown(30))
print(countdown(5)) 
print(countdown(15))

#Print and Return: Create a function that will receive a list with two numbers. Print the first value and return the second. 
#Example: print_and_return([1,2]) should pring 1 and return 2. 
def print_and_return(nums_list):
    print(nums_list[0])
    return nums_list[1]
print(print_and_return([1,2]))
