# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:09:48 2021

@author: Himadri Sen Gupta
"""

#Name: Himadri Sen Gupta 
#OUID: 113486497 





#Problem 1
#The German mathematician Gottfried Leibniz developed the following method to approximate the value of π: 𝜋4⁄=1−13⁄+15⁄−17⁄+⋯
#Write a program that allows the user to specify the number of iterations used in this approximation and that displays the resulting value of 𝜋.""

iterations = int(input("Enter the number of interations you want to consider for calculating pi value: "))

#aa is the variable which is taken to calculate the right hand side of the equation 
aa = 0


#this for loop will help to find the value of pi 

#if I know the number of iteration that means I have to go upto that number. we can get the value of denumerator by applying the formula = (2*iterations -1) As I want to catch 
#also the last number so in range function I have to add 2. 

for i in range(1, ((2*iterations) - 1)+2, 2):
    if i % 4 == 1:
        aa += 1/i
    else:
        aa -= 1/i 

pi = 4 * aa

#print the result 
print("The value of pi is ----->", pi)





#Problem 2
#Write a program that receives a series of numbers from the user and allows the user to press the Enter key to indicate that he or she
#is finished providing inputs. After the user presses the Enter key, the program should print the sum of the numbers and their average.


#count variable is used to track the number of input 
count = 0 

#initially the value of sum=0 as we still doesn't add anything 
sum = 0 

#This while loop will help to take the input before entering "Enter:" 
while True: 
    
    x = input("Enter the number or press Enter to break: ")
    if x  == "" :
        print ("Number is not entred")
        print ("The sum is--->", sum)
        break
    else: 
        count +=1
        sum = float (x) + sum
average = sum / count 

print("The average is--->" , average)






#Problem 3
#Teachers in most school districts are paid on a schedule that provides a salary based on their number of years of teaching experience. 
#For example, a beginning teacher in the Lexington School District might be paid $30,000 the first year. For each year of experience after 
#this first year, up to 10 years, the teacher receives a 2% increase over the preceding value. Write a program that displays a salary schedule, 
#in tabular format, for teachers in a school district. The inputs are the starting salary, the percentage increase, and the number of years in
#the schedule. Each row in the schedule should contain the year number and the salary for that year.

#this input function will ask for percentage increage of salary each year
i = float(input("Enter the percentage increase: "))

#this input function will take the initial salary
s = float(input("Enter the initial salary: "))

#this input function will take the the number of service year
y = int(input("Enter the number of service year: "))

salary = s

if y > 10: 
    print("This code is not applicable for the value of year more than 10")
else:
    print ("     Year    |    Salary  ")
    print("_____________|_______________")
    for a in range(y+1):
        if a == 0:
            salary = s
            print (a,"                ",salary)   #This will give the salary of the joining year
            print("_____________|_______________")
        else: 
            salary = salary + salary*(i/100) 
            print (a,"                ",salary)   ##This will give the salary of the next years 
            print("_____________|_______________")
 





#Problem 4
#In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7, the player wins $4; otherwise, the player loses $1.
#Suppose that, to entice the gullible, a casino tells players that there are lots of ways to win: (1,6), (2,5), and so on. A little mathematical 
#analysis reveals that there are not enough ways to win to make the game worthwhile; however, because many people’s eyes glaze over at the first
#mention of mathematics, your challenge is to write a program that demonstrates the futility of playing the game. Your program should take as 
#input the amount of money that the player wants to put into the pot and play the game until the pot is empty. At that point, the program should
#print the number of rolls it took to break the player, as well as maximum amount of money in the pot.

#import the random module so that random numbers can be genarated 
import random 

#input the initial amount 
amount = int(input("How much money would you like to put?:" ))  


#Have to start game with money 
if (amount<=0):
    
    print("Enter amount greater than 0")

else: 
    print("Let's play the game!!! ")
    
    #count is used to track number of rolls it took to break the player
    count = 0

    #this emply list is created so that I can put all the result here and find out the maximum amount of money from this list. 
    list_amount =[]


    #This while loop will ensure that the player can only play when s/he has money 
    while (amount > 0):   
        dice1 = random.randint(1,6) #Provide a random number for first dice
        dice2 = random.randint(1,6) #Provide a random number for second dice
        total = dice1 + dice2       #Provide the total of dice1 and dice 2
         
        if total == 7:
            amount  = amount  + 4 #Winning will add $4
        else: 
            amount  = amount  - 1 #If loss we will reduce $1
        count = count + 1
  
        list_amount.append(amount)
    
    print("The the number of rolls it took to break the player is : ", count)

    print("The maximum amount of money in the pot is: ", max(list_amount));   #max() function is used to find out the maximum amount of money in the pot during the entire game. 

print("******The game is end******")















