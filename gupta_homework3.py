# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:09:19 2021

@author: Himadri Sen Gupta
"""

#Name: Himadri Sen Gupta 
#OUID: 113486497




#Problem - 1 

#A group of statisticians at a local college has asked you to create a set of functions that compute the median and mode of a set of numbers. 
#Also include a function named mean, which computes the average of a set of numbers, and a function named standardDeviation that returns the 
#standard deviation of those numbers. Each function should expect a list of numbers as an argument and return a single number. Each function 
#should return 0 if the list is empty. Include a main function that tests the four statistical functions with a given list.
#HINT: you can import stats module and use built-in functions.

def main():
    
    #importing statistics module for calculating mode, median, standard deviation and mean 
    import statistics as stat
    
    #creating a blank list for taking the list from the user so that we can work on that 
    list = []
    while True:
        x = input("Enter the elements of the list or presss enter to exit: ")
        if x == "":
            print("End of inserting elements in the list")
            break;
        else:
            list.append(int(x));
            
    #This will just show us the imported list from the user 
    print("Your imported list is ---->", list) 

#This function will calculate the median of imported list 
    def median(list):
        return stat.median(list);

#This function will calculate the mean of imported list 
    def mean(list):
        return stat.mean(list);
    
#This function will calculate the mode of imported list 
    def mode(list):
        return stat.mode(list);
    
#This function will calculate the standard deviation of imported list 
    def standardDeviation(list):
        return stat.stdev(list);
    
    md = median(list)   
    print("The median of the list is --->", md);
    
    mn = mean(list)    
    print("The mean of the list is --->", mn);   
    
    mo = mode(list)  
    print("The mode of the list is --->", mo);
    
    std = standardDeviation(list)   
    print("The standard deviation of the list is --->", std);
    
main()
    
    
    
#Problem - 2 

#Write the Fibonacci sequence as a linear (non-recursive) algorithm. Let the function take in the desired term in the Fibonacci 
#sequence, and return the appropriate number. For example, the sequence starts as 1, 1, 2, 3, 5, 8, 13, …, so if the number 4
#was passed as the argument, 3 would be returned as it is the 4th term in the sequence.

def feb (n):

        #Taking a new black list for keep all the elements of the Fibonacchi Sequance 
    x = []    
   
    #Looping over the range of temrs so that I can preapre the series 
    for i in range (n):  
        if i == 0 or i == 1:                 
            x.append(1)            
        else:              
            x.append(x[i-2] + x[i-1])
            
    #Print the entire series in a form of list s 
    print ("The created Fibonacchi sequance is as follows --->", x)

#List[-1] always gives us the last number of the list 
    return (x[-1]);  
    

n = int (input("Enter the number of terms you want to consider for making sequence: "))

#number of terms can be only positive and if user input positive number then the function will run 
if n>1:    
    print("The last number of the sequence is ---->", feb(n))

#If anyone provide any negative number then s/he will get this notice of providing positive number 
else: 
    print("Enter a number greater than 0")
    


#Python’s pow function returns the result of raising a number to a given power. Define a function expo that performs this task. 
#The first argument of this function is the number, and the second argument is the exponent (non-negative numbers only). 
#You may use either a loop or a recursive function in your implementation.
#CAUTION: do not use Python’s ** operator or pow function in this exercise!


def expo(b, p):

    
#If the power of any number is 0, the result will be 1. 
    if p == 0:
        result = 1
        return result
#if the power is any other positive number then 
    else: 
       result = 1
       
       for i in range(p):         
           result = result * b
       return(result)


#Taking input of base 
b = int (input("Enter the base: "))

#Taking input of power 
p = int (input("Enter the power of the base: "))

result = expo(b, p)


print("The power of ", p, " in the base of " , b, "give the result of ", result ) 
















