#Basic: Print all integers from 0 to 150. 
def basic():
    for i in range(151):
        print(i)

basic() #don't forget, the function needs to be called. 

#Multiples of Five: Print all the multiples of 5 from 5 to 1,000
def multiples_of_five():
    for i in range(5, 1001, 5):
        print(i)

multiples_of_five()

#Counting, the Dojo Way: Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def the_dojo_way():
    for i in range(1,101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else: 
            print(i)

the_dojo_way()