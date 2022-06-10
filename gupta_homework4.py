# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:08:28 2021

@author: Himadri SEN GUPTA
"""

#Problem - 1 


from gurobipy import *

nodes = ['Warehouse - 1','Warehouse - 2', 'Retailer - 1', 'Retailer - 2', 'Retailer - 3', 'Retailer - 4', 'Retailer - 5', 'Dummy Node' ]


arcs, cost = multidict({('Warehouse - 1', 'Retailer - 1') : 2, 
                        ('Warehouse - 1','Retailer - 2') : 4,
                        ('Warehouse - 1','Retailer - 3' ) : 5,
                        ('Warehouse - 1','Retailer - 4' ) : 2,
                        ('Warehouse - 1','Retailer - 5' ) : 1,
                        ('Warehouse - 1','Dummy Node' ) : 0,
                        ('Warehouse - 2','Retailer - 1' ) : 3,
                        ('Warehouse - 2','Retailer - 2' ) : 1,
                        ('Warehouse - 2','Retailer - 3' ) : 3,
                        ('Warehouse - 2','Retailer - 4' ) : 2,
                        ('Warehouse - 2','Retailer - 5' ) : 3,
                        ('Warehouse - 2','Dummy Node' ) : 0})


#Positive values in this list indicates that those are Supply Nodes and negative values means those are demand nodes
in_flow =  {'Warehouse - 1': 2000,
            'Warehouse - 2': 3000,
            'Retailer - 1': -500,
            'Retailer - 2': -800,
            'Retailer - 3': -1800, 
            'Retailer - 4': -300,
            'Retailer - 5': -700, 
            'Dummy Node': -900}


# Create the model as an object
model = Model ("Problem - 1")

# Mute the Gurobi
model.setParam ('OutputFlag', False)


# Create the decison variables for each link
X = model.addVars(arcs, vtype=GRB.INTEGER, lb=0,ub=GRB.INFINITY, name="x")

for i in nodes:
    model.addConstr((quicksum(X[i,j] for i,j in arcs.select (i,'*')) - quicksum(X[j, i] for j, i in arcs.select ('*', i)) == in_flow[i]))

           

#Define the objective function
z = quicksum(X[i,j] * cost[i,j] for i,j in arcs)

# Specify the type of the model: minimization or maximization
model.setObjective (z, GRB.MINIMIZE)

# Update the model
model.update()

# Solve the model    
model.optimize()     
        
# Print out the optimal solutions: the decion variables values
model.printAttr ('x') 

# Print out the outputs

# Print out the outputs

if model.status==GRB.OPTIMAL:
    print ("-----------------------------------------")
    print ("Optimal value: $",model.objVal)
    print ("-----------------------------------------")
    print ("--- Quantity (origin to destination)---")
    for i, j  in arcs: 
            print ("From",i, "To ", j, X[i,j].X)

 

#Problem - 2 

#Importing Gurobi for solving the model 
from gurobipy import *

#Creating the list of nodes i 
nodes = ['Tempa', 'Miami', 'Fresno',  'New York', 'Philadelphia', 'Chicago', 'Boston', 'Dummy Demand Node' ]

#This multi-dict is used defining the arcs and cost related to that arcs 
arcs, cost = multidict({('Tempa', 'New York') : 9, 
                        ('Tempa','Philadelphia') : 14,
                        ('Tempa','Chicago') : 12,
                        ('Tempa','Boston') : 17,
                        ('Tempa','Dummy Demand Node' ) : 0,
                        ('Miami', 'New York') : 11, 
                        ('Miami','Philadelphia') : 10,
                        ('Miami','Chicago') : 60000,
                        ('Miami','Boston') : 10,
                        ('Miami','Dummy Demand Node' ) : 0,
                        ('Fresno', 'New York') : 12, 
                        ('Fresno','Philadelphia') : 8,
                        ('Fresno','Chicago') : 15,
                        ('Fresno','Boston') : 7,
                        ('Fresno','Dummy Demand Node' ) : 0,})

#This variable shows the demand and supply of earch nodes, positive value 
#means that the node is supply node and neegative value means demand nodes
in_flow =  {'Tempa' : 200,
            'Miami' : 200,
            'Fresno' : 200,  
            'New York': -130,
            'Philadelphia' : -170,
            'Chicago': -100,
            'Boston': -150, 
            'Dummy Demand Node' : -50 }

# Create the model as an object
model = Model ("Problem - 2")

# Mute the Gurobi
model.setParam ('OutputFlag', False)


# Create the decison variables for each link
X = model.addVars(arcs, vtype=GRB.INTEGER, lb=0,ub=GRB.INFINITY, name="x")

#Flow balance constraints 
for i in nodes:
    model.addConstr((quicksum(X[i,j] for i,j in arcs.select (i,'*')) - quicksum(X[j, i] for j, i in arcs.select ('*', i)) == in_flow[i]))

           

#Define the objective function
z = quicksum(X[i,j] * cost[i,j] for i,j in arcs)

# Specify the type of the model: minimization or maximization
model.setObjective (z, GRB.MINIMIZE)

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
    print ("--- Quantity (origin to destination)---")
    for i, j  in arcs: 
            print ("From",i, "To ", j, X[i,j].X)




#Problem - 3 



#Importing Gurobi for solving the model 
from gurobipy import *

#Creating the list of nodes i 
nodes = ['Ohio', 'Pennsylvania', 'New York', 'Dummy Supply Node', 'Indiana', 'Georgia', 'Virginia', 'Kentucky', 'Lousiana']

#This multi-dict is used defining the arcs and cost related to that arcs 
arcs, cost = multidict({('Ohio', 'Indiana') : 16, 
                        ('Ohio','Georgia') : 21,
                        ('Pennsylvania','Indiana' ) : 18,
                        ('Pennsylvania','Georgia' ) : 16,
                        ('New York','Indiana' ) : 22,
                        ('New York', 'Georgia') : 25,
                        ('Indiana', 'Virginia'): 23,
                        ('Indiana', 'Kentucky'): 15,
                        ('Indiana', 'Lousiana'): 29, 
                        ('Georgia', 'Virginia') : 20, 
                        ('Georgia', 'Kentucky') : 17,
                        ('Georgia', 'Lousiana') : 24,
                        ('Dummy Supply Node', 'Indiana') : 0,
                        ('Dummy Supply Node', 'Georgia') : 0})

#This variable shows the demand and supply of earch nodes, positive value 
#means that the node is supply node and neegative value means demand nodes

in_flow =  {'Ohio' : 72, 
            'Pennsylvania': 105, 
            'New York': 83, 
            'Dummy Supply Node': 30, 
            'Indiana': 0,
            'Georgia': 0, 
            'Virginia': -90, 
            'Kentucky': -80,
            'Lousiana' : -120 }


# Create the model as an object
model = Model ("transportation")

# Mute the Gurobi
model.setParam ('OutputFlag', False)


# Create the decison variables for each link
X = model.addVars(arcs, vtype=GRB.INTEGER, lb=0,ub=GRB.INFINITY, name="x")

#Constraints for ensuring that we are not exceeding the capacity of plants: 
model.addConstr(X['Ohio', 'Indiana'] + X['Pennsylvania', 'Indiana'] + X['New York', 'Indiana'] <= 140)
    
model.addConstr(X['Ohio', 'Georgia'] + X['Pennsylvania', 'Georgia'] + X['New York', 'Georgia'] <= 140)

#Flow balance constraints 
for i in nodes:
    model.addConstr((quicksum(X[i,j] for i,j in arcs.select (i,'*')) - quicksum(X[j, i] for j, i in arcs.select ('*', i)) == in_flow[i]));
          

#Define the objective function
z = quicksum(X[i,j] * cost[i,j] for i,j in arcs)

# Specify the type of the model: minimization or maximization
model.setObjective (z, GRB.MINIMIZE)

# Update the model
model.update()

# Solve the model    
model.optimize()     
        
# Print out the optimal solutions: the decion variables values
model.printAttr ('x') 

# Print out the outputs

# Print out the outputs

if model.status==GRB.OPTIMAL:
    print ("-----------------------------------------")
    print ("Optimal value: $",model.objVal)
    print ("-----------------------------------------")
    print ("--- Quantity (origin to destination)---")
    for i, j  in arcs: 
            print ("From",i, "To ", j, X[i,j].X)

#Problem - 4 

from gurobipy import *
events = ['Alumni Brunch', 'Parents Brunch', 'Booster Club Lunch', 'Postgame Party', 'Lettermens Dinner', 'Contributors Dinner' ]



two_event_handler = ['Bon Apetit', 'Custom', 'University']

one_event_handler = ['Als', 'Divine', 'Epicurean', 'Fouchess']


link_2, cost_2 = multidict({ 
          ('Bon Apetit', 'Alumni Brunch'): 14.5, ('Bon Apetit', 'Parents Brunch'): 13, ('Bon Apetit', 'Booster Club Lunch'): 16.5,
          ('Bon Apetit', 'Postgame Party'): 17,('Bon Apetit', 'Lettermens Dinner'): 22.5,('Bon Apetit', 'Contributors Dinner'): 32,
          ('Custom', 'Alumni Brunch'): 13, ('Custom', 'Parents Brunch'): 14, ('Custom', 'Booster Club Lunch'): 17.6,
          ('Custom', 'Postgame Party'): 21.5,('Custom', 'Lettermens Dinner'): 23,('Custom', 'Contributors Dinner'): 35,
          ('University', 'Alumni Brunch'): 12.5, ('University', 'Parents Brunch'): 14.3, ('University', 'Booster Club Lunch'): 16,
          ('University', 'Postgame Party'): 22,('University', 'Lettermens Dinner'): 26.7,('University', 'Contributors Dinner'): 34})


link_1, cost_1 = multidict({
          ('Als', 'Alumni Brunch'): 12.6, ('Als', 'Parents Brunch'): 10.3, ('Als', 'Booster Club Lunch'): 14.0,
          ('Als', 'Postgame Party'): 19.5,('Als', 'Lettermens Dinner'): 25,('Als', 'Contributors Dinner'): 30,
          ('Divine', 'Alumni Brunch'): 11.5, ('Divine', 'Parents Brunch'): 12.6, ('Divine', 'Booster Club Lunch'): 13,
          ('Divine', 'Postgame Party'): 18.7,('Divine', 'Lettermens Dinner'): 26.2,('Divine', 'Contributors Dinner'): 33.5,
          ('Epicurean', 'Alumni Brunch'): 10.8, ('Epicurean', 'Parents Brunch'): 11.9, ('Epicurean', 'Booster Club Lunch'): 12.9,
          ('Epicurean', 'Postgame Party'): 17.5,('Epicurean', 'Lettermens Dinner'): 21.9,('Epicurean', 'Contributors Dinner'): 28.5,  
          ('Fouchess', 'Alumni Brunch'): 13.5, ('Fouchess', 'Parents Brunch'): 13.5, ('Fouchess', 'Booster Club Lunch'): 15.5,
          ('Fouchess', 'Postgame Party'): 22.3,('Fouchess', 'Lettermens Dinner'): 24.5,('Fouchess', 'Contributors Dinner'): 36})


# Create the model as an object
model = Model ("Problem - 4")

# Mute the Gurobi
model.setParam ('OutputFlag', False)

# Create the decison variables for each link
X = model.addVars(two_event_handler,events, vtype=GRB.BINARY, lb=0,ub=1, name="x")

Y = model.addVars(one_event_handler,events, vtype=GRB.BINARY, lb=0,ub=1, name="y")



#All the events are covered with at least on caterer 
for j in events: model.addConstr((quicksum(X[i, j] for i in two_event_handler)) + (quicksum(Y[k, j] for k in one_event_handler)) == 1)

#Some caterer can serve 2 events 
for i in two_event_handler:  model.addConstr((quicksum(X[i,j] for j in events)) <= 2)

#Some caterer can serve only 1 events     
for k in one_event_handler: model.addConstr((quicksum(Y[k,j] for j in events)) <= 1)

      

#Define the objective function
z = quicksum(X[i,j] * cost_2[i,j] for i,j in link_2 ) + quicksum(Y[i,j] * cost_1[i,j] for i,j in link_1)

# Specify the type of the model: minimization or maximization
model.setObjective (z, GRB.MINIMIZE)

# Update the model
model.update()

# Solve the model    
model.optimize()     
        
# Print out the optimal solutions: the decion variables values
model.printAttr ('x') 

# Print out the outputs

if model.status==GRB.OPTIMAL:
    print ("-----------------------------------------")
    print ("The minimum cost of handling all these event is: $",model.objVal)
    print ("-----------------------------------------")
    print ("---------- Caterer Assignment Result -----------")
    for i, j in link_2: 
        if X[i,j].X == 1:  
            
            print (j, "should be handled by", i)
    
    for i, j in link_1: 
        if Y[i,j].X == 1:  
            
            print (j, "should be handled by", i)
       


















