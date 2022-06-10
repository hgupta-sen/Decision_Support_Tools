
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 00:10:32 2021

@author: hgupt
"""

#Problem - 2 

#Importing Gurobi for solving the model 
from gurobipy import *
import networkx as nx
import matplotlib.pyplot as plt


#Creating the list of nodes i 
nodes = ['Factory - 1', 'Factory - 2', 'Warehouse - 1', 'Warehouse - 2', 'Distribution Center']

#This multi-dict is used defining the arcs and cost related to that arcs 
arcs, cost, ubound, lbound= multidict({('Factory - 1', 'Warehouse - 1') : [6, 1000000, 0],  
                        ('Factory - 2','Warehouse - 2') : [9,1000000, 0],
                        ('Factory - 1','Distribution Center') : [2, 50, 0],
                        ('Factory - 2','Distribution Center') : [4, 50, 0],
                        ('Distribution Center','Warehouse - 1' ) : [3,50, 0],
                        ('Distribution Center','Warehouse - 2' ) :[4, 50, 0]})


#This variable shows the demand and supply of earch nodes, positive value 
#means that the node is supply node and neegative value means demand nodes
in_flow =  {'Factory - 1' : 80,
            'Factory - 2' : 70,
            'Warehouse - 1' : -60, 
            'Warehouse - 2' : -90, 
            'Distribution Center' : 0}
            #'Dummy Demand Node' : -1200}

# Create the model as an object
model = Model ("Problem - 3")

# Mute the Gurobi
model.setParam ('OutputFlag', False)


# Create the decison variables for each link
X = model.addVars(arcs, vtype=GRB.INTEGER, lb=0,ub=GRB.INFINITY, name="x")

# model.addConstr(X['Factory - 1','Distribution Center'] <= 50)
# model.addConstr(X['Factory - 2','Distribution Center'] <= 50)
# model.addConstr(X['Distribution Center','Warehouse - 1'] <= 50)
# model.addConstr(X['Distribution Center','Warehouse - 2'] <= 50)   
    
#Flow balance constraints 
for i in nodes:
    model.addConstr((quicksum(X[i,j] for i,j in arcs.select (i,'*')) - quicksum(X[j, i] for j, i in arcs.select ('*', i)) == in_flow[i]))

# model.addConstr(X[i,j] <= ub)         
for i, j in arcs:
    model.addConstr(X[i,j] <= ubound[i,j])   
    
for i, j in arcs:
    model.addConstr(lbound[i,j] <=X[i,j]) 
    
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
    print ("Optimal value: $",model.objVal)
    print ("-----------------------------------------")
    print ("--- Quantity (origin to destination)---")
    for i, j  in arcs: 
            print ("From",i, "To ", j, X[i,j].X)



G = nx.DiGraph()

G.add_edges_from(arcs)

pos = nx.spring_layout(G)   

nx.draw_circular(G, edge_color='red',node_shape = '8', width=2,node_size=500,node_color='green', alpha=0.8,\
labels={node:node for node in G.nodes()})

plt.show()

# Network information
# -----------------------
print(nx.info(G))
print(G.nodes())
print (G.edges())

#Centrality measures : 
# ---------------------------------    
print ("degree ---> ", G.degree())    
dg_cen = nx.degree_centrality(G)