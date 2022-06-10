# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 00:57:26 2021

@author: Himadri Sen Gupta
"""

# Import gurobi
from gurobipy import *

# Define the model parameters 

# List containing plant 
Alloys = ['Alloy - 1', 'Alloy - 2', 'Alloy - 3', 'Alloy - 4', 'Alloy - 5'] 

# List containing warehouse  
Property = ['Tin', 'Zinc', 'Lead']    

# Dictionary containing costs of the oils
cost_o = {'Alloy - 1': 22,
          'Alloy - 2': 26, 
          'Alloy - 3': 25, 
          'Alloy - 4': 21, 
          'Alloy - 5': 27 }

# Dictionary containing daily availability of the oils
available_o = {'Tin': 35,
               'Zinc': 35,
               'Lead': 30}

com, percentage = multidict({('Alloy - 1', 'Tin'): 60,
                             ('Alloy - 2', 'Tin'): 25,
                             ('Alloy - 3', 'Tin'): 45,
                             ('Alloy - 4', 'Tin'): 30,
                             ('Alloy - 5', 'Tin'): 50,
                             ('Alloy - 1', 'Zinc'): 20,
                             ('Alloy - 2', 'Zinc'): 15,
                             ('Alloy - 3', 'Zinc'): 45,
                             ('Alloy - 4', 'Zinc'): 40,
                             ('Alloy - 5', 'Zinc'): 40,
                             ('Alloy - 1', 'Lead'): 20,
                             ('Alloy - 2', 'Lead'): 60,
                             ('Alloy - 3', 'Lead'): 10,
                             ('Alloy - 4', 'Lead'): 30,
                             ('Alloy - 5', 'Lead'): 10                                                      
                             })
# Dictionary containing revenue of each blend
# revenue_b = {blend[0]: 1.1, blend[1]: 1.2}

# Create the model as an object
model = Model ("Problem - 2")

# Mute the Gurobi
# model.setParam ('OutputFlag', False)

# Create the decison variables for each link showing flow from plant points to warehouse points
X = model.addVars(Alloys, vtype=GRB.CONTINUOUS, lb=0,ub=GRB.INFINITY, name="x")


# Amount of oil available 
# for i in oil:
#     model.addConstr(quicksum(X[i,j] for j in blend) <= available_o[i])

# # long term contract requirements:
# for j in blend:
#     model.addConstr(quicksum(X[i,j] for i in oil) >= 10000)
   
# # Requirement on the composition of the fuels

for i in Property: 
    model.addConstr(quicksum(X[j] *   percentage [j,i] for j in Alloys) == available_o[i])
    
model.addConstr(quicksum(X[j]for j in Alloys) == 1)    

# # blend 1
# for j in blend:
#     if j=='b1':
#         model.addConstr (X['A',j] >= 0.3 * quicksum(X[i,j]for i in oil))
#         model.addConstr (X['B',j] <= 0.5 * quicksum(X[i,j]for i in oil))
#         model.addConstr (X['C',j] >= 0.3 * quicksum(X[i,j]for i in oil))

# # blend 2
#     else:
#         model.addConstr (X['A',j] <= 0.4 * quicksum(X[i,j]for i in oil))
#         model.addConstr (X['B',j] >= 0.35 * quicksum(X[i,j]for i in oil))
#         model.addConstr (X['C',j] <= 0.4 * quicksum(X[i,j]for i in oil))



# Define the objective function
Z = quicksum(X[i] * cost_o[i] for i in Alloys)

# Specify the type of the model:  maximizing the profit
model.setObjective (Z, GRB.MINIMIZE)

# Update the model
model.update()

# Solve the model    
model.optimize()     
        
# Print out the optimal solutions: the decion variables values
model.printAttr ('x') 


# Print out the outputs

if model.status==GRB.OPTIMAL:
    print ("-----------------------------------------")
    print ("Optimal value: $",model.objVal)
    print ("-----------------------------------------")
    for i in Alloys:
            print ( "Proportion of ", i ," used" , X[i].X * 100, "%")
   






