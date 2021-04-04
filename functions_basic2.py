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
