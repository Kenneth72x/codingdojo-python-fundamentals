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

#First Plus Length: Create a function that accepts a list and returns the sum of the first value in the list plust the list's length. 
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(nums_list):
    return nums_list[0] + len(nums_list)

print(first_plus_length([1,2,3,4,5]))

#Values Greater than Second: Write a function that accepts a list and creates a new list containing only the values from the original list that are greater
#than its second value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False. 
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return false. 
def values_greater_than_second(orig_list):
    new_list = []
    second_val = orig_list[1]
    for idx in range(len(orig_list)):
        if orig_list[idx] > second_val:
            new_list.append(orig_list[idx])

    print(len(new_list))
    return new_list  

print(values_greater_than_second([5,2,3,2,1,4]))
