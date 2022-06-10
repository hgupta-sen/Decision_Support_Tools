# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:31:58 2021

@author: Himadri Sen Gupta 
"""


#OUID: 113486497 

#Importing Gurobi for solving the model 
from gurobipy import *
import networkx as nx
import matplotlib.pyplot as plt


#Creating the list of nodes i 
nodes = ['Factory - 1', 'Factory - 2', 'Warehouse - 1', 'Warehouse - 2', 
         'Wholesaler - 1', 'Wholesaler - 2', 'Wholesaler - 3', 'Wholesaler - 4']


#This multi-dict is used defining the arcs and cost related to that arcs 
arcs, cost= multidict({('Factory - 1', 'Warehouse - 1') : 40,  
                        ('Factory - 1','Warehouse - 2') : 35,
                        ('Factory - 2','Warehouse - 2') : 25,
                        ('Warehouse - 1','Wholesaler - 1') :60,
                        ('Warehouse - 1','Wholesaler - 2') :35,
                        ('Warehouse - 2','Wholesaler - 2') :55,
                        ('Warehouse - 2','Wholesaler - 3') :50,
                        ('Warehouse - 2','Wholesaler - 4') : 65})


#-------------------PART - A ------------------------------------------------
G = nx.DiGraph()

G.add_edges_from(arcs)

pos = nx.spring_layout(G)   

nx.draw_circular(G, edge_color='black',node_shape = 'o', width=2,node_size=500,node_color='pink', alpha=0.8,\
labels={node:node for node in G.nodes()})

plt.show()

# Network information
print(nx.info(G))
print(G.nodes())
print (G.edges())

#Centrality measures :   
print ("degree ---> ", G.degree())    
dg_cen = nx.degree_centrality(G)

#-------------------PART - B ------------------------------------------------


#This variable shows the demand and supply of earch nodes, positive value 
#means that the node is supply node and neegative value means demand nodes

in_flow =  {'Factory - 1': 400, 
            'Factory - 2': 350, 
            'Warehouse - 1' : 0, 
            'Warehouse - 2' : 0, 
            'Wholesaler - 1' : -200, 
            'Wholesaler - 2' : -100, 
            'Wholesaler - 3' : -150, 
            'Wholesaler - 4' : -200} 

# Create the model as an object
model = Model ("Mid-Term Exam 2 Problem")

# Mute the Gurobi
model.setParam ('OutputFlag', False)


# Create the decison variables for each link
X = model.addVars(arcs, vtype=GRB.INTEGER, lb=0,ub=GRB.INFINITY, name="x")

    
#Flow balance constraints 
for i in nodes:
    model.addConstr((quicksum(X[i,j] for i,j in arcs.select (i,'*')) - quicksum(X[j, i] for j, i in arcs.select ('*', i)) <= in_flow[i]))


#Capacity of Warehouse 1 is 200 
model.addConstr(X['Factory - 1', 'Warehouse - 1'] <= 200) 


#Capacity of the arc from Factory 2 to Warehouse 2 is 300 
model.addConstr(X['Factory - 2','Warehouse - 2'] <= 300)  
    
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

#Print out the outputs
if model.status==GRB.OPTIMAL:
    print ("-----------------------------------------")
    print ("Optimal Annual Transportation Cost: $",model.objVal)
    print ("-----------------------------------------")
    print ("--- Quantity (origin to destination)---")
    for i, j  in arcs: 
            print ("From",i, "To ", j, X[i,j].X)



