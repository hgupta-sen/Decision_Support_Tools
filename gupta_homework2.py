# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:58:55 2021

@author: Himadri Sen Gupta
"""


#Name: Himadri Sen Gupta 
#OUID: 113486497


#Problem - 1 


#Write a program to display the Fibonacci sequence up to n-th term. The program should prompt the user for the number of terms.
#Note that a Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8.... The first two terms are 0 and 1. All other 
#terms are obtained by adding the preceding two terms.



#Providing the number of terms I want to consider 
n = int(input("Enter the number of terms: "))

#Opening a blank loop for keeping the terms of Fibonacci Sequance 
x = []


#Looping over the range of temrs so that I can preapre the series 
for i in range (n):  
    if i == 0:
        x.append(0)
    elif i== 1:
        x.append(1)
    else:
        x.append(x[i-2] + x[i-1])
 
#Print the entire series in a form of list s 
print (x); 


#Problem - 2 

#The payroll department keeps a list of employee information for each pay period in a text file named payroll.txt. The format of each line of the file is as follows:
#< name > < hourlywage > < hoursworked >
#Write a program that inputs the filename: payroll.txt from the user and prints to the terminal a report of the wages paid to the employees for the given period. 
#The report should be in tabular format with the appropriate header. Each line should contain an employee’s name, the hours worked, and the wages paid for that period. You can find payroll.txt in Assignment #2 on Canvas.

#importing prettytable for creating the table 
from prettytable import PrettyTable
#Giving the name of file in the program
file = input("Enter the file name you want to consider for calculation: ")

#Opeing the file in reading mode
fr = open(file, "r")

#Printing the header
t = PrettyTable(["Name", "Hourly Wages", "Hours Worked","Total Pay"])


#Looping over the text file for doing calculation of wages 
for line in fr.readlines():

    cols = line.strip().split()
    t.add_row([cols[0],float(cols[1]),float(cols[2]), (float(cols[1]) * float(cols[2]))])


#printing the tablular formated result 
print(t)

#Closing the file after the calculation 
fr.close() 



#Problem - 3



#Write a program that prompts the user for the names of two text files including: myfile1.txt and myfile2.txt. The contents of the first file, myfile1.txt, 
#should be input and written to the second file, myfile2.txt. You can find myfile1.txt in Assignment #2 on Canvas.



#Taking the name of the first file from where the sencond file will read the data 
file1 = input("Enter the file name you want to copy from: ")

#Opeing the first text file in reading mode 
fr1 = open(file1, "r")

#Taking the name of second file which will be created and keep the data of first file
file2 = input("Enter the file name you want to write: ")

#Opening the second file in writing mode so that we can wirte in it from the first file. 
fw = open(file2, "w")


#Looping over the first file for writing in the second file 
for line in fr1:
    fw.write(line)
  
#Closing the second file so that I can re-open it for reading 
fw.close()

#Reopeing the second file in reading mode, because when the file in writing mode, it can't read the file. 
f = open(file2, "r")

#Looping over the second file for printing as well as checking is it running or not. 
for l in f:
    print(l)
    
#Closing the running files 
f.close()
fr1.close() 
   