#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:42:35 2021

@author:Himadri Sen Gupta
"""

from gurobipy import *
import networkx as nx
import matplotlib.pyplot as plt

# List containing suuply points 
supply_p = ['Plant - 1', 'Plant - 2', 'Plant - 3'] 


# List containing transshipment points    
transshipment_p = ['Warehouse - 1', 'Warehouse - 2']  

# List containing demand points    
demand_p = ['Distribution Center - 1', 'Distribution Center - 2']  

cost_inst = {'Plant - 1': 15000, 
             'Plant - 2': 18000,
             'Plant - 3': 22000}
# Dictionary containing the tarnsportaion cost information between the points
cost_t = {('Plant - 1', 'Warehouse - 1') : 70, 
        ('Plant - 1','Warehouse - 2') : 73,
        ('Plant - 2','Warehouse - 1') : 69,
        ('Plant - 2','Warehouse - 2') : 71,
        ('Plant - 3','Warehouse - 1') : 68,
        ('Plant - 3','Warehouse - 2') : 70,
        ('Warehouse - 1','Distribution Center - 1' ) : 23,
        ('Warehouse - 1','Distribution Center - 2' ) : 28,
        ('Warehouse - 2','Distribution Center - 1' ) : 27,
        ('Warehouse - 2','Distribution Center - 2' ) : 22}


arcs,cost_t = multidict(cost_t)
print ("demand points", demand_p)
print ("transshipment points", transshipment_p)
print ("supply points", supply_p)


# Dictionary containing amount of supply at each origion point (supply point)
supply_v = {
'Plant - 1' : 700,
            'Plant - 2' : 800,
            'Plant - 3' : 1000
    }


# Dictionary containing demand required at each destination point (demand point)
demand_v = {
            'Distribution Center - 1' : 700,
            'Distribution Center - 2' : 600
    }

print ("supply", supply_v)
print ("demand", demand_v)

print ("transportation cost", cost_t)
# Import gurobi
from gurobipy import *


# Create the model as an object
model = Model ("transshipment")

# Mute the Gurobi
# model.setParam ('OutputFlag', False)


# Create the decison variables for each link from supply points to trashsipment points
X = model.addVars(supply_p, transshipment_p, vtype=GRB.INTEGER, lb=0,ub=GRB.INFINITY, name="x")

# Create the decison variables for each link from trashsipment points to demand points
Y = model.addVars(transshipment_p, demand_p, vtype=GRB.INTEGER, lb=0,ub=GRB.INFINITY, name="y")

Z = model.addVars(supply_p, vtype=GRB.BINARY, lb=0,ub=1, name="Z")


for i in supply_p:
    for j in transshipment_p:
        model.addConstr(X[i,j] + 1000000 * (1 - Z[i]) >= 0)

for i in supply_p:
    for j in transshipment_p:
        
        model.addConstr(X[i,j]  <= 0 + 1000000 * Z[i])
    
  
# Supply constraints
for i in supply_p:
    model.addConstr(quicksum(X[i,j] for j in transshipment_p) <= supply_v[i])

# Demand constraints
for j in demand_p:
    model.addConstr(quicksum(Y[i,j] for i in transshipment_p) == demand_v[j])

# Transshipment constraints: Balance constraints
for i in transshipment_p:
    model.addConstr((quicksum(Y[i,j] for j in demand_p) - quicksum(X[k, i] for k in supply_p) == 0))


# Define the objective function
Z = quicksum(X[i,j] * cost_t[i,j] for i in supply_p for j in transshipment_p)+ quicksum(Y[m,n] * cost_t[m,n] for m in transshipment_p for n in demand_p) + quicksum(Z[i] * cost_inst[i] for i in supply_p)

# Specify the type of the model: minimization or maximization
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
    print ("--- Quantity (From - To) ---")
    for i in supply_p: 
        for j in transshipment_p:
            print ("From",i, "To ", j, X[i,j].X)
    for i in transshipment_p: 
        for j in demand_p:
            print ("From",i, "To ", j, Y[i,j].X)
            
            
G = nx.DiGraph()

G.add_edges_from(arcs)

pos = nx.spring_layout(G)   

nx.draw_circular(G, edge_color='black',node_shape = '8', width=2,node_size=500,node_color='green', alpha=0.8,\
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