# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:42:30 2021

@author: hgupt
"""

#--------------Importing Libraries-------------------------#

from gurobipy import *
import networkx as nx
import matplotlib.pyplot as plt


#-----------Some Printing Statement-----------------#
                                       
print("\nLets Make Our Vacation Plan !!!")

print("\nHey, Which type of activities you would like to do ??  ")

print("\nYou can write anything like - Hiking, Beach, Winter Sports, Others  ")

x = input("\nThe activity will be : ")

Answer = input("\nWhat is your priority? Money ??? Time???? Both ??? ")
    
Hotel = input("\nWhat type of hotel you would like to prefer? One Star? Three Star ? Five Star ? ")

print("[[Instructions: For entering stay time, please enter at most 8 days]]")

Duration = int(input("\nHow many days you want to stay in the hotel?? "))

time_constraint = float (input("\nHow much time you want to travel during this vacation?? "))


    


#--------------Data Set-------------------------#


#------------------------------HIKING------------------------#

nodes_hiking_one = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Charlotte (CLT)", 
                	"Denver (DEN)", "Phoenix (PHX)", 	"Salt Lake City (SLC)", "1-Star"]

nodes_hiking_three = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Charlotte (CLT)", 
                	"Denver (DEN)", "Phoenix (PHX)", 	"Salt Lake City (SLC)", "3-Star"]

nodes_hiking_five = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Charlotte (CLT)", 
                	"Denver (DEN)", "Phoenix (PHX)", 	"Salt Lake City (SLC)", "5-Star"]

inflow_hiking_one = {"OKC": 1, "Delta":0 , "American Airlines":0, "United":0, "Southwest":0, "Frontier":0, "Charlotte (CLT)": 0, 
                	"Denver (DEN)": 0, "Phoenix (PHX)": 0, 	"Salt Lake City (SLC)": 0, "1-Star":-1}

inflow_hiking_three = {"OKC": 1, "Delta":0 , "American Airlines":0, "United":0, "Southwest":0, "Frontier":0, "Charlotte (CLT)": 0, 
                	"Denver (DEN)": 0, "Phoenix (PHX)": 0, 	"Salt Lake City (SLC)": 0, 	"3-Star":-1}

inflow_hiking_five = {"OKC": 1, "Delta":0 , "American Airlines":0, "United":0, "Southwest":0, "Frontier":0, "Charlotte (CLT)": 0, 
                	"Denver (DEN)": 0, "Phoenix (PHX)": 0, 	"Salt Lake City (SLC)": 0, "5-Star":-1}


arcs_hiking_one, cost_hiking_one, time_hiking_one = multidict({ ("OKC", "Delta" ): [0, 0], 
                                      ("OKC", "American Airlines"): [0,0], 
                                      ("OKC", "United"): [0,0], 
                                      ("OKC", "Southwest"): [0,0] ,
                                      ("OKC", "Frontier"): [0,0] ,
                                      ("Delta", "Charlotte (CLT)") : [444.9, 3.53],
                                      ("Delta", "Denver (DEN)"): [212.4, 5.32],
                                      ("Delta", "Phoenix (PHX)"): [447.4,5.42],
                                      ("Delta", "Salt Lake City (SLC)"): [427.8 , 2.42],                
                                      ("American Airlines", "Charlotte (CLT)") : [566, 2.44],
                                      ("American Airlines", "Denver (DEN)"): [151, 4.17],
                                      ("American Airlines", "Phoenix (PHX)"): [455,2.38],
                                      ("American Airlines", "Salt Lake City (SLC)"): [424, 5.22],
                                      ("United", "Charlotte (CLT)") : [445, 5],
                                      ("United", "Denver (DEN)"): [195, 1.5],
                                      ("United", "Phoenix (PHX)"): [473,4.36],
                                      ("United", "Salt Lake City (SLC)"): [424, 4],
                                      ("Southwest", "Charlotte (CLT)") : [237, 4.05],
                                      ("Southwest", "Denver (DEN)"): [113, 1.25],
                                      ("Southwest", "Phoenix (PHX)"): [228, 2.25],
                                      ("Southwest", "Salt Lake City (SLC)"): [237, 4],
                                      ("Frontier", "Charlotte (CLT)") : [139, 13.25],
                                      ("Frontier", "Denver (DEN)"): [132, 1.41],
                                      ("Frontier", "Phoenix (PHX)"): [270, 7.56],
                                      ("Frontier", "Salt Lake City (SLC)"): [325, 12.5],

                                      ("Charlotte (CLT)","1-Star"): [67 * Duration, 1],

                                      ("Denver (DEN)","1-Star"): [54 * Duration, 1],

                                      ("Phoenix (PHX)","1-Star"): [69 * Duration, 1],

                                      ("Salt Lake City (SLC)","1-Star"): [52 * Duration, 1]
                                      })

arcs_hiking_three, cost_hiking_three, time_hiking_three = multidict({ ("OKC", "Delta" ): [0, 0], 
                                      ("OKC", "American Airlines"): [0,0], 
                                      ("OKC", "United"): [0,0], 
                                      ("OKC", "Southwest"): [0,0] ,
                                      ("OKC", "Frontier"): [0,0] ,
                                      ("Delta", "Charlotte (CLT)") : [444.9, 3.53],
                                      ("Delta", "Denver (DEN)"): [212.4, 5.32],
                                      ("Delta", "Phoenix (PHX)"): [447.4,5.42],
                                      ("Delta", "Salt Lake City (SLC)"): [427.8 , 2.42],                
                                      ("American Airlines", "Charlotte (CLT)") : [566, 2.44],
                                      ("American Airlines", "Denver (DEN)"): [151, 4.17],
                                      ("American Airlines", "Phoenix (PHX)"): [455,2.38],
                                      ("American Airlines", "Salt Lake City (SLC)"): [424, 5.22],
                                      ("United", "Charlotte (CLT)") : [445, 5],
                                      ("United", "Denver (DEN)"): [195, 1.5],
                                      ("United", "Phoenix (PHX)"): [473,4.36],
                                      ("United", "Salt Lake City (SLC)"): [424, 4],
                                      ("Southwest", "Charlotte (CLT)") : [237, 4.05],
                                      ("Southwest", "Denver (DEN)"): [113, 1.25],
                                      ("Southwest", "Phoenix (PHX)"): [228, 2.25],
                                      ("Southwest", "Salt Lake City (SLC)"): [237, 4],
                                      ("Frontier", "Charlotte (CLT)") : [139, 13.25],
                                      ("Frontier", "Denver (DEN)"): [132, 1.41],
                                      ("Frontier", "Phoenix (PHX)"): [270, 7.56],
                                      ("Frontier", "Salt Lake City (SLC)"): [325, 12.5],

                                      ("Charlotte (CLT)","3-Star"): [115* Duration, 1],

                                      ("Denver (DEN)","3-Star"): [121* Duration, 1],

                                      ("Phoenix (PHX)","3-Star"): [116* Duration, 1],

                                      ("Salt Lake City (SLC)","3-Star"): [105* Duration, 1],

                                      })

arcs_hiking_five, cost_hiking_five, time_hiking_five = multidict({ ("OKC", "Delta" ): [0, 0], 
                                      ("OKC", "American Airlines"): [0,0], 
                                      ("OKC", "United"): [0,0], 
                                      ("OKC", "Southwest"): [0,0] ,
                                      ("OKC", "Frontier"): [0,0] ,
                                      ("Delta", "Charlotte (CLT)") : [444.9, 3.53],
                                      ("Delta", "Denver (DEN)"): [212.4, 5.32],
                                      ("Delta", "Phoenix (PHX)"): [447.4,5.42],
                                      ("Delta", "Salt Lake City (SLC)"): [427.8 , 2.42],                
                                      ("American Airlines", "Charlotte (CLT)") : [566, 2.44],
                                      ("American Airlines", "Denver (DEN)"): [151, 4.17],
                                      ("American Airlines", "Phoenix (PHX)"): [455,2.38],
                                      ("American Airlines", "Salt Lake City (SLC)"): [424, 5.22],
                                      ("United", "Charlotte (CLT)") : [445, 5],
                                      ("United", "Denver (DEN)"): [195, 1.5],
                                      ("United", "Phoenix (PHX)"): [473,4.36],
                                      ("United", "Salt Lake City (SLC)"): [424, 4],
                                      ("Southwest", "Charlotte (CLT)") : [237, 4.05],
                                      ("Southwest", "Denver (DEN)"): [113, 1.25],
                                      ("Southwest", "Phoenix (PHX)"): [228, 2.25],
                                      ("Southwest", "Salt Lake City (SLC)"): [237, 4],
                                      ("Frontier", "Charlotte (CLT)") : [139, 13.25],
                                      ("Frontier", "Denver (DEN)"): [132, 1.41],
                                      ("Frontier", "Phoenix (PHX)"): [270, 7.56],
                                      ("Frontier", "Salt Lake City (SLC)"): [325, 12.5],
                                      ("Charlotte (CLT)","5-Star"): [238* Duration, 1], 

                                      ("Denver (DEN)","5-Star"): [383* Duration,  1],

                                      ("Phoenix (PHX)","5-Star"): [667* Duration, 1] ,

                                      ("Salt Lake City (SLC)","5-Star"): [373* Duration,  1],

                                      })


#------------------------------Winter Sports------------------------#


nodes_wintersports_one = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Allegiant", "Chicago Midway (MDW)", 
                	"Chicago O'Hare (ORD)", "Denver (DEN)", 	"Minneapolis (MSP)",  "1-Star"]

nodes_wintersports_three = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Allegiant", "Chicago Midway (MDW)", 
                	"Chicago O'Hare (ORD)", "Denver (DEN)", 	"Minneapolis (MSP)", "3-Star"]

nodes_wintersports_five = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Allegiant", "Chicago Midway (MDW)", 
                	"Chicago O'Hare (ORD)", "Denver (DEN)", 	"Minneapolis (MSP)", "5-Star"]


inflow_wintersports_one = {"OKC": 1, "Delta": 0 , "American Airlines": 0, "United": 0, "Southwest": 0, "Frontier": 0, "Allegiant": 0,
                       "Chicago Midway (MDW)": 0, "Chicago O'Hare (ORD)": 0, "Denver (DEN)": 0, "Minneapolis (MSP)": 0, "1-Star": -1}

inflow_wintersports_three = {"OKC": 1, "Delta": 0 , "American Airlines": 0, "United": 0, "Southwest": 0, "Frontier": 0, "Allegiant": 0,
                       "Chicago Midway (MDW)": 0, "Chicago O'Hare (ORD)": 0, "Denver (DEN)": 0, "Minneapolis (MSP)": 0, "3-Star": -1}

inflow_wintersports_five = {"OKC": 1, "Delta": 0 , "American Airlines": 0, "United": 0, "Southwest": 0, "Frontier": 0, "Allegiant": 0,
                       "Chicago Midway (MDW)": 0, "Chicago O'Hare (ORD)": 0, "Denver (DEN)": 0, "Minneapolis (MSP)": 0, "5-Star": -1}

arcs_wintersports_one, cost_wintersports_one, time_wintersports_one = multidict({ ("OKC", "Delta" ): [0, 0],
                                      ("OKC", "American Airlines"): [0,  0],
                                      ("OKC", "United"): [0, 0],
                                      ("OKC", "Southwest"): [0, 0],
                                      ("OKC", "Frontier"): [0,  0],
                                      ("Delta", "Chicago Midway (MDW)") : [386.5,4.45],
                                      ("Delta", "Chicago O'Hare (ORD)"): [386.5, 4.39],
                                      ("Delta", "Denver (DEN)"): [212.4,5.32],
                                      ("Delta", "Minneapolis (MSP)"): [477.8, 2.13],                
                                      ("American Airlines", "Chicago O'Hare (ORD)"): [369, 2.13], 
                                      ("American Airlines", "Denver (DEN)"): [151, 4.17],
                                      ("American Airlines", "Minneapolis (MSP)"): [251, 7],
                                      ("United", "Chicago O'Hare (ORD)"): [369, 2.09],
                                      ("United", "Denver (DEN)"): [195, 1.5],
                                      ("United", "Minneapolis (MSP)"): [371, 4.34],
                                      ("Southwest", "Chicago Midway (MDW)") :[185 , 1.55],
                                      ("Southwest", "Chicago O'Hare (ORD)"): [194, 5.3],
                                      ("Southwest", "Denver (DEN)"): [113, 1.35],
                                      ("Southwest", "Minneapolis (MSP)"): [194, 4.2],
                                      ("Frontier", "Chicago O'Hare (ORD)"): [270 , 11.29], 
                                      ("Frontier", "Denver (DEN)"): [132, 1.41], 
                                      ("Frontier", "Minneapolis (MSP)"): [270, 11.5], 

                                      ("Chicago Midway (MDW)","1-Star"): [106* Duration, 1],

                                      ("Chicago O'Hare (ORD)","1-Star"): [106* Duration, 1],

                                      ("Denver (DEN)","1-Star"): [54* Duration, 1],

                                      ("Minneapolis (MSP)","1-Star"): [66* Duration, 1]
                                      })

arcs_wintersports_three, cost_wintersports_three, time_wintersports_three = multidict({ ("OKC", "Delta" ): [0, 0],
                                      ("OKC", "American Airlines"): [0,  0],
                                      ("OKC", "United"): [0, 0],
                                      ("OKC", "Southwest"): [0, 0],
                                      ("OKC", "Frontier"): [0,  0],
                                      ("Delta", "Chicago Midway (MDW)") : [386.5,4.45],
                                      ("Delta", "Chicago O'Hare (ORD)"): [386.5, 4.39],
                                      ("Delta", "Denver (DEN)"): [212.4,5.32],
                                      ("Delta", "Minneapolis (MSP)"): [477.8, 2.13],                
                                      ("American Airlines", "Chicago O'Hare (ORD)"): [369, 2.13], 
                                      ("American Airlines", "Denver (DEN)"): [151, 4.17],
                                      ("American Airlines", "Minneapolis (MSP)"): [251, 7],
                                      ("United", "Chicago O'Hare (ORD)"): [369, 2.09],
                                      ("United", "Denver (DEN)"): [195, 1.5],
                                      ("United", "Minneapolis (MSP)"): [371, 4.34],
                                      ("Southwest", "Chicago Midway (MDW)") :[185 , 1.55],
                                      ("Southwest", "Chicago O'Hare (ORD)"): [194, 5.3],
                                      ("Southwest", "Denver (DEN)"): [113, 1.35],
                                      ("Southwest", "Minneapolis (MSP)"): [194, 4.2],
                                      ("Frontier", "Chicago O'Hare (ORD)"): [270 , 11.29], 
                                      ("Frontier", "Denver (DEN)"): [132, 1.41], 
                                      ("Frontier", "Minneapolis (MSP)"): [270, 11.5], 

                                      ("Chicago Midway (MDW)","3-Star"): [121* Duration, 1],

                                      ("Chicago O'Hare (ORD)","3-Star"): [121* Duration, 1],

                                      ("Denver (DEN)","3-Star"): [121* Duration, 1],

                                      ("Minneapolis (MSP)","3-Star"): [87* Duration, 1],

                                      })

arcs_wintersports_five, cost_wintersports_five, time_wintersports_five = multidict({ ("OKC", "Delta" ): [0, 0],
                                      ("OKC", "American Airlines"): [0,  0],
                                      ("OKC", "United"): [0, 0],
                                      ("OKC", "Southwest"): [0, 0],
                                      ("OKC", "Frontier"): [0,  0],
                                      ("Delta", "Chicago Midway (MDW)") : [386.5,4.45],
                                      ("Delta", "Chicago O'Hare (ORD)"): [386.5, 4.39],
                                      ("Delta", "Denver (DEN)"): [212.4,5.32],
                                      ("Delta", "Minneapolis (MSP)"): [477.8, 2.13],                
                                      ("American Airlines", "Chicago O'Hare (ORD)"): [369, 2.13], 
                                      ("American Airlines", "Denver (DEN)"): [151, 4.17],
                                      ("American Airlines", "Minneapolis (MSP)"): [251, 7],
                                      ("United", "Chicago O'Hare (ORD)"): [369, 2.09],
                                      ("United", "Denver (DEN)"): [195, 1.5],
                                      ("United", "Minneapolis (MSP)"): [371, 4.34],
                                      ("Southwest", "Chicago Midway (MDW)") :[185 , 1.55],
                                      ("Southwest", "Chicago O'Hare (ORD)"): [194, 5.3],
                                      ("Southwest", "Denver (DEN)"): [113, 1.35],
                                      ("Southwest", "Minneapolis (MSP)"): [194, 4.2],
                                      ("Frontier", "Chicago O'Hare (ORD)"): [270 , 11.29], 
                                      ("Frontier", "Denver (DEN)"): [132, 1.41], 
                                      ("Frontier", "Minneapolis (MSP)"): [270, 11.5], 
                                      ("Chicago Midway (MDW)","5-Star"): [411* Duration, 1], 

                                      ("Chicago O'Hare (ORD)","5-Star"): [411* Duration,  1],

                                      ("Denver (DEN)","5-Star"): [383* Duration,  1],

                                      ("Minneapolis (MSP)","5-Star"): [135* Duration,  1],
                                      })


#------------------------------Beach------------------------#

nodes_beach_one = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Allegiant", "Houston Hobby (HOU)", 
                	"Houston International (IAH)", "Seattle (SEA)", "1-Star"]

nodes_beach_three = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Allegiant", "Houston Hobby (HOU)", 
                	"Houston International (IAH)", "Seattle (SEA)", "3-Star"]

nodes_beach_five = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Allegiant", "Houston Hobby (HOU)", 
                	"Houston International (IAH)", "Seattle (SEA)", "5-Star"]

inflow_beach_one = {"OKC" : 1, "Delta" : 0, "American Airlines": 0, "United": 0, "Southwest": 0, "Frontier": 0, "Allegiant": 0, "Houston Hobby (HOU)": 0, 
                	"Houston International (IAH)": 0, "Seattle (SEA)": 0, "1-Star":-1}

inflow_beach_three = {"OKC" : 1, "Delta" : 0, "American Airlines": 0, "United": 0, "Southwest": 0, "Frontier": 0, "Allegiant": 0, "Houston Hobby (HOU)": 0, 
                	"Houston International (IAH)": 0, "Seattle (SEA)": 0, "3-Star":-1}

inflow_beach_five = {"OKC" : 1, "Delta" : 0, "American Airlines": 0, "United": 0, "Southwest": 0, "Frontier": 0, "Allegiant": 0, "Houston Hobby (HOU)": 0, 
                	"Houston International (IAH)": 0, "Seattle (SEA)": 0, "5-Star":-1}

arcs_beach_one, cost_beach_one, time_beach_one = multidict({ 
                                      ("OKC", "Delta"): [0, 0],
                                      ("OKC", "American Airlines"):[0, 0], 
                                      ("OKC", "United"): [0, 0],
                                      ("OKC", "Southwest"): [0, 0],
                                      ("OKC", "Frontier"): [0, 0], 
                                      ("Delta", "Houston Hobby (HOU)") : [872, 4.49],
                                      ("Delta", "Houston International (IAH)"): [872, 5],
                                      ("Delta", "Seattle (SEA)"): [268.4, 5.46],                                       
                                      ("American Airlines", "Houston Hobby (HOU)") : [343, 4.49],
                                      ("American Airlines", "Houston International (IAH)"):[343 ,5],
                                      ("American Airlines", "Seattle (SEA)"): [269, 9.7],
                                      ("United", "Houston International (IAH)"): [325, 3.18],
                                      ("United", "Seattle (SEA)"): [269, 6.22],
                                      ("Southwest", "Houston Hobby (HOU)") : [163, 1.25],
                                      ("Southwest", "Houston International (IAH)"):[172, 5.35],
                                      ("Southwest", "Seattle (SEA)"): [148, 5.55],
                                      ("Frontier", "Seattle (SEA)"):[302 ,  21.43],                                     

                                      ("Houston Hobby (HOU)","1-Star"): [37* Duration, 1],
 
                                      ("Houston International (IAH)","1-Star"): [37* Duration,1],

                                      ("Seattle (SEA)","1-Star"): [98* Duration, 1]

                                      })

arcs_beach_three, cost_beach_three, time_beach_three = multidict({ 
                                      ("OKC", "Delta"): [0, 0],
                                      ("OKC", "American Airlines"):[0, 0], 
                                      ("OKC", "United"): [0, 0],
                                      ("OKC", "Southwest"): [0, 0],
                                      ("OKC", "Frontier"): [0, 0], 
                                      ("Delta", "Houston Hobby (HOU)") : [872, 4.49],
                                      ("Delta", "Houston International (IAH)"): [872, 5],
                                      ("Delta", "Seattle (SEA)"): [268.4, 5.46],                                       
                                      ("American Airlines", "Houston Hobby (HOU)") : [343, 4.49],
                                      ("American Airlines", "Houston International (IAH)"):[343 ,5],
                                      ("American Airlines", "Seattle (SEA)"): [269, 9.7],
                                      ("United", "Houston International (IAH)"): [325, 3.18],
                                      ("United", "Seattle (SEA)"): [269, 6.22],
                                      ("Southwest", "Houston Hobby (HOU)") : [163, 1.25],
                                      ("Southwest", "Houston International (IAH)"):[172, 5.35],
                                      ("Southwest", "Seattle (SEA)"): [148, 5.55],
                                      ("Frontier", "Seattle (SEA)"):[302 ,  21.43],                                     

                                      ("Houston Hobby (HOU)","3-Star"): [120* Duration,1],

                                      ("Houston International (IAH)","3-Star"): [120* Duration,1],

                                      ("Seattle (SEA)","3-Star"): [126* Duration,1],


                                      })

arcs_beach_five, cost_beach_five, time_beach_five = multidict({ 
                                      ("OKC", "Delta"): [0, 0],
                                      ("OKC", "American Airlines"):[0, 0], 
                                      ("OKC", "United"): [0, 0],
                                      ("OKC", "Southwest"): [0, 0],
                                      ("OKC", "Frontier"): [0, 0], 
                                      ("Delta", "Houston Hobby (HOU)") : [872, 4.49],
                                      ("Delta", "Houston International (IAH)"): [872, 5],
                                      ("Delta", "Seattle (SEA)"): [268.4, 5.46],                                       
                                      ("American Airlines", "Houston Hobby (HOU)") : [343, 4.49],
                                      ("American Airlines", "Houston International (IAH)"):[343 ,5],
                                      ("American Airlines", "Seattle (SEA)"): [269, 9.7],
                                      ("United", "Houston International (IAH)"): [325, 3.18],
                                      ("United", "Seattle (SEA)"): [269, 6.22],
                                      ("Southwest", "Houston Hobby (HOU)") : [163, 1.25],
                                      ("Southwest", "Houston International (IAH)"):[172, 5.35],
                                      ("Southwest", "Seattle (SEA)"): [148, 5.55],
                                      ("Frontier", "Seattle (SEA)"):[302 ,  21.43],                                     
                                      ("Houston Hobby (HOU)","5-Star"): [380* Duration, 1],
  
                                      ("Houston International (IAH)","5-Star"): [380* Duration,1 ],

                                      ("Seattle (SEA)","5-Star"): [473* Duration, 1],

                                      })

#------------------------------Others------------------------#


nodes_others_one = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Allegiant", "Atlanta (ATL)", 
                	"Charlotte (CLT)", "Dallas Ft Worth (DFW)", "Las Vegas (LAS)", "Nashville (BNA)", "St. Louis (STL)","1-Star"]

nodes_others_three = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Allegiant", "Atlanta (ATL)", 
                	"Charlotte (CLT)", "Dallas Ft Worth (DFW)", "Las Vegas (LAS)", "Nashville (BNA)", "St. Louis (STL)","3-Star"]

nodes_others_five = ["OKC", "Delta" , "American Airlines", "United", "Southwest", "Frontier", "Allegiant", "Atlanta (ATL)", 
                	"Charlotte (CLT)", "Dallas Ft Worth (DFW)", "Las Vegas (LAS)", "Nashville (BNA)", "St. Louis (STL)","5-Star"]

inflow_others_one = {"OKC": 1, "Delta"  : 0, "American Airlines" : 0, "United" : 0, "Southwest" : 0, "Frontier" : 0, "Allegiant" : 0, "Atlanta (ATL)" : 0, 
                	"Charlotte (CLT)" : 0, "Dallas Ft Worth (DFW)" : 0, "Las Vegas (LAS)" : 0, "Nashville (BNA)" : 0, "St. Louis (STL)" : 0, "1-Star": -1}

inflow_others_three = {"OKC": 1, "Delta"  : 0, "American Airlines" : 0, "United" : 0, "Southwest" : 0, "Frontier" : 0, "Allegiant" : 0, "Atlanta (ATL)" : 0, 
                	"Charlotte (CLT)" : 0, "Dallas Ft Worth (DFW)" : 0, "Las Vegas (LAS)" : 0, "Nashville (BNA)" : 0, "St. Louis (STL)" : 0, "3-Star": -1}

inflow_others_five = {"OKC": 1, "Delta"  : 0, "American Airlines" : 0, "United" : 0, "Southwest" : 0, "Frontier" : 0, "Allegiant" : 0, "Atlanta (ATL)" : 0, 
                	"Charlotte (CLT)" : 0, "Dallas Ft Worth (DFW)" : 0, "Las Vegas (LAS)" : 0, "Nashville (BNA)" : 0, "St. Louis (STL)" : 0, "5-Star": -1,}




arcs_others_one, cost_others_one, time_others_one = multidict({ ("OKC", "Delta" ): [0, 0 ],
                                      ("OKC", "American Airlines"): [0, 0 ],
                                      ("OKC", "United"): [0, 0],
                                      ("OKC", "Southwest"): [0, 0],
                                      ("OKC", "Frontier"): [0, 0 ],
                                      ("OKC", "Allegiant"): [0, 0 ],
                                      ("Delta", "Atlanta (ATL)") : [345.8, 2],
                                      ("Delta", "Charlotte (CLT)"): [444.9, 3.53],
                                      ("Delta", "Las Vegas (LAS)"): [282.4, 5.32 ],  
                                      ("Delta", "Nashville (BNA)"): [361.4, 4],
                                      ("Delta", "St. Louis (STL)"): [339.4, 4.21],
                                      ("American Airlines", "Atlanta (ATL)") : [362, 4.15],
                                      ("American Airlines", "Charlotte (CLT)"): [566, 2.44],
                                      ("American Airlines", "Dallas Ft Worth (DFW)"): [491, 1.11],
                                      ("American Airlines", "Las Vegas (LAS)"): [343, 5.17],
                                      ("American Airlines", "Nashville (BNA)"): [360, 4.22],
                                      ("American Airlines", "St. Louis (STL)"): [389, 6],
                                      ("United", "Atlanta (ATL)") : [364, 4.17],
                                      ("United", "Charlotte (CLT)"): [445, 5],
                                      ("United", "Dallas Ft Worth (DFW)"): [639, 3.45],
                                      ("United", "Las Vegas (LAS)"): [443, 4.33],
                                      ("United", "Nashville (BNA)"): [362, 4.14],
                                      ("United", "St. Louis (STL)"): [340, 4.26],
                                      ("Southwest", "Atlanta (ATL)") : [228, 2],
                                      ("Southwest", "Charlotte (CLT)"): [237, 4.05],
                                      ("Southwest", "Las Vegas (LAS)"): [207, 4.15],
                                      ("Southwest", "Nashville (BNA)"): [184, 3.15],
                                      ("Southwest", "St. Louis (STL)"): [163, 1.25],
                                      ("Frontier", "Atlanta (ATL)") : [217, 8],
                                      ("Frontier", "Charlotte (CLT)"): [139, 13.25],
                                      ("Frontier", "Las Vegas (LAS)"): [487, 13.39],
                                      ("Frontier", "Nashville (BNA)"): [270, 22],
                                      ("Frontier", "St. Louis (STL)"): [140, 21.12],
                                      ("Allegiant", "Las Vegas (LAS)"): [120, 4.3],

                                      ("Atlanta (ATL)","1-Star"): [53* Duration, 1],
  
                                      ("Charlotte (CLT)","1-Star"): [67* Duration,1 ],

                                      ("Dallas Ft Worth (DFW)","1-Star"): [56* Duration,1 ],

                                      ("Las Vegas (LAS)","1-Star"): [63* Duration,1 ],

                                      ("Nashville (BNA)","1-Star"): [74* Duration, 1],

                                      ("Las Vegas (LAS)","1-Star"): [63* Duration, 1],

                                      ("St. Louis (STL)","1-Star"): [57* Duration, 1]
                                      })

arcs_others_three, cost_others_three, time_others_three = multidict({ ("OKC", "Delta" ): [0, 0 ],
                                      ("OKC", "American Airlines"): [0, 0 ],
                                      ("OKC", "United"): [0, 0],
                                      ("OKC", "Southwest"): [0, 0],
                                      ("OKC", "Frontier"): [0, 0 ],
                                      ("OKC", "Allegiant"): [0, 0 ],
                                      ("Delta", "Atlanta (ATL)") : [345.8, 2],
                                      ("Delta", "Charlotte (CLT)"): [444.9, 3.53],
                                      ("Delta", "Las Vegas (LAS)"): [282.4, 5.32 ],  
                                      ("Delta", "Nashville (BNA)"): [361.4, 4],
                                      ("Delta", "St. Louis (STL)"): [339.4, 4.21],
                                      ("American Airlines", "Atlanta (ATL)") : [362, 4.15],
                                      ("American Airlines", "Charlotte (CLT)"): [566, 2.44],
                                      ("American Airlines", "Dallas Ft Worth (DFW)"): [491, 1.11],
                                      ("American Airlines", "Las Vegas (LAS)"): [343, 5.17],
                                      ("American Airlines", "Nashville (BNA)"): [360, 4.22],
                                      ("American Airlines", "St. Louis (STL)"): [389, 6],
                                      ("United", "Atlanta (ATL)") : [364, 4.17],
                                      ("United", "Charlotte (CLT)"): [445, 5],
                                      ("United", "Dallas Ft Worth (DFW)"): [639, 3.45],
                                      ("United", "Las Vegas (LAS)"): [443, 4.33],
                                      ("United", "Nashville (BNA)"): [362, 4.14],
                                      ("United", "St. Louis (STL)"): [340, 4.26],
                                      ("Southwest", "Atlanta (ATL)") : [228, 2],
                                      ("Southwest", "Charlotte (CLT)"): [237, 4.05],
                                      ("Southwest", "Las Vegas (LAS)"): [207, 4.15],
                                      ("Southwest", "Nashville (BNA)"): [184, 3.15],
                                      ("Southwest", "St. Louis (STL)"): [163, 1.25],
                                      ("Frontier", "Atlanta (ATL)") : [217, 8],
                                      ("Frontier", "Charlotte (CLT)"): [139, 13.25],
                                      ("Frontier", "Las Vegas (LAS)"): [487, 13.39],
                                      ("Frontier", "Nashville (BNA)"): [270, 22],
                                      ("Frontier", "St. Louis (STL)"): [140, 21.12],
                                      ("Allegiant", "Las Vegas (LAS)"): [120, 4.3],

                                      ("Atlanta (ATL)","3-Star"): [116* Duration,1 ],

                                      ("Charlotte (CLT)","3-Star"): [115* Duration,1 ],

                                      ("Dallas Ft Worth (DFW)","3-Star"): [147* Duration,1 ],

                                      ("Las Vegas (LAS)","3-Star"): [82* Duration,1 ],

                                      ("Nashville (BNA)","3-Star"): [155* Duration,1 ],

                                      ("Las Vegas (LAS)","3-Star"): [82* Duration,1 ],

                                      ("St. Louis (STL)","3-Star"): [113* Duration,1 ],

                                      })


arcs_others_five, cost_others_five, time_others_five = multidict({ ("OKC", "Delta" ): [0, 0 ],
                                      ("OKC", "American Airlines"): [0, 0 ],
                                      ("OKC", "United"): [0, 0],
                                      ("OKC", "Southwest"): [0, 0],
                                      ("OKC", "Frontier"): [0, 0 ],
                                      ("OKC", "Allegiant"): [0, 0 ],
                                      ("Delta", "Atlanta (ATL)") : [345.8, 2],
                                      ("Delta", "Charlotte (CLT)"): [444.9, 3.53],
                                      ("Delta", "Las Vegas (LAS)"): [282.4, 5.32 ],  
                                      ("Delta", "Nashville (BNA)"): [361.4, 4],
                                      ("Delta", "St. Louis (STL)"): [339.4, 4.21],
                                      ("American Airlines", "Atlanta (ATL)") : [362, 4.15],
                                      ("American Airlines", "Charlotte (CLT)"): [566, 2.44],
                                      ("American Airlines", "Dallas Ft Worth (DFW)"): [491, 1.11],
                                      ("American Airlines", "Las Vegas (LAS)"): [343, 5.17],
                                      ("American Airlines", "Nashville (BNA)"): [360, 4.22],
                                      ("American Airlines", "St. Louis (STL)"): [389, 6],
                                      ("United", "Atlanta (ATL)") : [364, 4.17],
                                      ("United", "Charlotte (CLT)"): [445, 5],
                                      ("United", "Dallas Ft Worth (DFW)"): [639, 3.45],
                                      ("United", "Las Vegas (LAS)"): [443, 4.33],
                                      ("United", "Nashville (BNA)"): [362, 4.14],
                                      ("United", "St. Louis (STL)"): [340, 4.26],
                                      ("Southwest", "Atlanta (ATL)") : [228, 2],
                                      ("Southwest", "Charlotte (CLT)"): [237, 4.05],
                                      ("Southwest", "Las Vegas (LAS)"): [207, 4.15],
                                      ("Southwest", "Nashville (BNA)"): [184, 3.15],
                                      ("Southwest", "St. Louis (STL)"): [163, 1.25],
                                      ("Frontier", "Atlanta (ATL)") : [217, 8],
                                      ("Frontier", "Charlotte (CLT)"): [139, 13.25],
                                      ("Frontier", "Las Vegas (LAS)"): [487, 13.39],
                                      ("Frontier", "Nashville (BNA)"): [270, 22],
                                      ("Frontier", "St. Louis (STL)"): [140, 21.12],
                                      ("Allegiant", "Las Vegas (LAS)"): [120, 4.3],
                                      ("Atlanta (ATL)","5-Star"): [400* Duration , 1 ],

                                      ("Charlotte (CLT)","5-Star"): [238* Duration,  1],

                                      ("Dallas Ft Worth (DFW)","5-Star"): [251* Duration, 1 ],

                                      ("Las Vegas (LAS)","5-Star"): [229* Duration, 1 ],

                                      ("Nashville (BNA)","5-Star"): [426* Duration, 1 ],

                                      ("Las Vegas (LAS)","5-Star"): [229* Duration, 1 ],

                                      ("St. Louis (STL)","5-Star"): [402* Duration, 1 ],

                                      })


#--------------Budget Function-------------------------#


#Function of budget calculation 
def budget_calculation(): 
    
    total_budget = int(input("\n\nEnter the budget of your travel: "))
    
    shopping = int(input("\n\nEnter the budget you want to have for the shopping and others: "))
    
    budget = total_budget - shopping 
    
    print ("\n\nSo your budget for travelling is: ", budget)
    
    return budget


#--------------Single Objective Optimization Function (Minimizing the Travel Cost)-------------------------#




#Function for running optimization model      
def optimization_function_money(budget, time_constraint,  nodes, arcs, cost, time, in_flow): 
    
    
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
    
    # Create the model as an object
    model = Model ("Vacation_Plan_Optimizar")
    
    # Mute the Gurobi
    #model.setParam ('OutputFlag', False)
    
    
    # Create the decison variables for each link
    X = model.addVars(arcs, vtype=GRB.BINARY, lb=0,ub=1, name="x")
    
    
    model.addConstr(quicksum(X[i,j] * cost[i,j] for i,j in arcs) <= budget)
    
    model.addConstr(quicksum(X[i,j] * time[i,j] for i,j in arcs) <= time_constraint)
    
    #Flow balance constraints 
    for i in nodes:
        model.addConstr((quicksum(X[i,j] for i,j in arcs.select (i,'*')) - quicksum(X[j, i] for j, i in arcs.select ('*', i)) >= in_flow[i]))
    
               
    
    #Define the objective function
    #z = quicksum((X[i,j] * cost[i,j] for i,j in arcs)) * mu_1  + (quicksum(X[i,j] * time[i,j] for i,j in arcs)) * mu_2
    z = quicksum((X[i,j] * cost[i,j] for i,j in arcs))
    # Specify the type of the model: minimization or maximization
    model.setObjective (z, GRB.MINIMIZE)
    
    # Update the model
    model.update()
    
    # Solve the model    
    model.optimize()     
            
    # Print out the optimal solutions: the decion variables values
    #model.printAttr ('x') 
    # if model.status == GRB.Status.OPTIMAL:
    #     best = 0
    #     for key in range(model.SolCount):
    #         model.setParam(GRB.Param.SolutionNumber, key)
    #         print ("Objective value:",model.PoolobjVal)
    #         model.printAttr ('xn')
    #         if model.objVal == model.PoolObjVal:
    #             print ("Objective value:",model.PoolobjVal)
    #             model.printAttr ('xn')
    #             best+=1
    
    # number of best solutions
    # print ("Number of solutions in which the objective value is equal to",model.objVal, "is:" , best)
    
    # Print out the outputs
    if model.status==GRB.OPTIMAL:
        print ("-----------------------------------------")
        print ("Optimal value:",model.objVal)
        model.printAttr ('x') 
    else: 
        print("Please Modify Your Budget or Expected Travel Time !!")



#--------------Single Objective Optimization Function (Minimizing the Travel Time)-------------------------#


#Function for running optimization model      
def optimization_function_time(budget, time_constraint, nodes, arcs, cost, time, in_flow): 
    
    
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
    
    # Create the model as an object
    model = Model ("Vacation_Plan_Optimizar")
    
    # Mute the Gurobi
    #model.setParam ('OutputFlag', False)
    
    
    # Create the decison variables for each link
    X = model.addVars(arcs, vtype=GRB.BINARY, lb=0,ub=1, name="x")
    
    
    model.addConstr(quicksum(X[i,j] * cost[i,j] for i,j in arcs) <= budget)
    
    model.addConstr(quicksum(X[i,j] * time[i,j] for i,j in arcs) <= time_constraint)
    
    #Flow balance constraints 
    for i in nodes:
        model.addConstr((quicksum(X[i,j] for i,j in arcs.select (i,'*')) - quicksum(X[j, i] for j, i in arcs.select ('*', i)) >= in_flow[i]))
    
               
    
    #Define the objective function
    #z = quicksum((X[i,j] * cost[i,j] for i,j in arcs)) * mu_1  + (quicksum(X[i,j] * time[i,j] for i,j in arcs)) * mu_2
    z = (quicksum(X[i,j] * time[i,j] for i,j in arcs))
    # Specify the type of the model: minimization or maximization
    model.setObjective (z, GRB.MINIMIZE)
    
    # Update the model
    model.update()
    
    # Solve the model    
    model.optimize()     
            
    # Print out the optimal solutions: the decion variables values
    # model.printAttr ('x') 
    # if model.status == GRB.Status.OPTIMAL:
    #     best = 0
    #     for key in range(model.SolCount):
    #         model.setParam(GRB.Param.SolutionNumber, key)
    #         print ("Objective value:",model.PoolobjVal)
    #         model.printAttr ('xn')
    #         if model.objVal == model.PoolObjVal:
    #             print ("Objective value:",model.PoolobjVal)
    #             model.printAttr ('xn')
    #             best+=1
    
    # number of best solutions
    #print ("Number of solutions in which the objective value is equal to",model.objVal, "is:" , best)
    
    # Print out the outputs
    if model.status==GRB.OPTIMAL:
        print ("-----------------------------------------")
        print ("Optimal value:",model.objVal)
        model.printAttr ('x') 
    else: 
        print("Please Modify Your Budget or Expected Travel Time !!")


#--------------Multi Objective Optimization Function (Minimizing the Travel Time & Minimizing the Travel Cost)-------------------------#


#Function for running optimization model      
def multi_optimization_function(budget, time_constraint, nodes, arcs, cost, time, in_flow): 
    
    
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
    
    # Create the model as an object
    model = Model ("Vacation_Plan_Optimizar")
    
    # Mute the Gurobi
    #model.setParam ('OutputFlag', False)
    
    
    # Create the decison variables for each link
    X = model.addVars(arcs, vtype=GRB.BINARY, lb=0,ub=1, name="x")
    
    model.addConstr(mu_1 + mu_2 == 1)
    
    
    model.addConstr(quicksum(X[i,j] * cost[i,j] for i,j in arcs) <= budget)
    
    model.addConstr(quicksum(X[i,j] * time[i,j] for i,j in arcs) <= time_constraint)
    
    #Flow balance constraints 
    for i in nodes:
        model.addConstr((quicksum(X[i,j] for i,j in arcs.select (i,'*')) - quicksum(X[j, i] for j, i in arcs.select ('*', i)) == in_flow[i]))
    
               
    
    #Define the objective function
    z = quicksum((X[i,j] * cost[i,j] for i,j in arcs)) * mu_1  + (quicksum(X[i,j] * time[i,j] for i,j in arcs)) * mu_2
    #z = (quicksum(X[i,j] * time[i,j] for i,j in arcs))
    # Specify the type of the model: minimization or maximization
    model.setObjective (z, GRB.MINIMIZE)
    
    # Update the model
    model.update()
    
    # Solve the model    
    model.optimize()     
            
    # Print out the optimal solutions: the decion variables values
    # model.printAttr ('x') 
    # if model.status == GRB.Status.OPTIMAL:
    #     best = 0
    #     for key in range(model.SolCount):
    #         model.setParam(GRB.Param.SolutionNumber, key)
    #         print ("Objective value:",model.PoolobjVal)
    #         model.printAttr ('xn')
    #         if model.objVal == model.PoolObjVal:
    #             print ("Objective value:",model.PoolobjVal)
    #             model.printAttr ('xn')
    #             best+=1
    
    # # number of best solutions
    # print ("Number of solutions in which the objective value is equal to",model.objVal, "is:" , best)
    
    # # Print out the outputs
    # if model.status==GRB.OPTIMAL:
    #     print ("-----------------------------------------")
    #     print ("Optimal value:",model.objVal)
        
    # else: 
    #     print("Please Modify Your Budget !!")
    
        # Print out the outputs
    if model.status==GRB.OPTIMAL:
        print ("-----------------------------------------")
        print ("Optimal value:",model.objVal)
        model.printAttr ('x') 
    else: 
        print("Please Modify Your Budget or Expected Travel Time !!")



#--------------Main Coding Section for calling the optimization function-------------------------#



budget = budget_calculation()


if budget > 0: 
    
    if Answer == "Money": 
        
        if x == "Hiking":
            
            if Hotel == "One Star": 
                optimization_function_money(budget, time_constraint, nodes_hiking_one, arcs_hiking_one, cost_hiking_one, time_hiking_one, inflow_hiking_one)
            elif Hotel == "Three Star": 
                optimization_function_money(budget, time_constraint, nodes_hiking_three, arcs_hiking_three, cost_hiking_three, time_hiking_three, inflow_hiking_three)
            else: 
                optimization_function_money(budget, time_constraint, nodes_hiking_five, arcs_hiking_five, cost_hiking_five, time_hiking_five, inflow_hiking_five)
        
        elif x == "Beach":
            
            if Hotel == "One Star": 
                optimization_function_money(budget, time_constraint, nodes_beach_one, arcs_beach_one, cost_beach_one, time_beach_one, inflow_beach_one)
            elif Hotel == "Three Star": 
                optimization_function_money(budget, time_constraint, nodes_beach_three, arcs_beach_three, cost_beach_three, time_beach_three, inflow_beach_three)
            else: 
                optimization_function_money(budget, time_constraint, nodes_beach_five, arcs_beach_five, cost_beach_five, time_beach_five, inflow_beach_five)

        
        elif x == "Winter Sports": 
            
            if Hotel == "One Star": 
                optimization_function_money(budget, time_constraint, nodes_wintersports_one, arcs_wintersports_one, cost_wintersports_one, time_wintersports_one, inflow_wintersports_one)
            elif Hotel == "Three Star": 
                optimization_function_money(budget, time_constraint, nodes_wintersports_three, arcs_wintersports_three, cost_wintersports_three, time_wintersports_three, inflow_wintersports_three)
            else : 
                optimization_function_money(budget, time_constraint, nodes_wintersports_five, arcs_wintersports_five, cost_wintersports_five, time_wintersports_five, inflow_wintersports_five)
                
            
 #           optimization_function_money(budget, nodes_wintersports, arcs_wintersports, cost_wintersports, time_wintersports, inflow_wintersports)
        
        else:
            
            if Hotel == "One Star": 
                optimization_function_money(budget, time_constraint, nodes_others_one, arcs_others_one, cost_others_one, time_others_one, inflow_others_one)
            elif Hotel == "Three Star": 
                optimization_function_money(budget, time_constraint, nodes_others_three, arcs_others_three, cost_others_three, time_others_three, inflow_others_three)
            else : 
                optimization_function_money(budget, time_constraint, nodes_others_five, arcs_others_five, cost_others_five, time_others_five, inflow_others_five)
                
            
    if Answer == "Time": 
        
        if x == "Hiking":
            
            if Hotel == "One Star": 
                optimization_function_time(budget, time_constraint, nodes_hiking_one, arcs_hiking_one, cost_hiking_one, time_hiking_one, inflow_hiking_one)
            elif Hotel == "Three Star": 
                optimization_function_time(budget, time_constraint, nodes_hiking_three, arcs_hiking_three, cost_hiking_three, time_hiking_three, inflow_hiking_three)
            else: 
                optimization_function_time(budget, time_constraint, nodes_hiking_five, arcs_hiking_five, cost_hiking_five, time_hiking_five, inflow_hiking_five)
        
        elif x == "Beach":
            
            if Hotel == "One Star": 
                optimization_function_time(budget, time_constraint, nodes_beach_one, arcs_beach_one, cost_beach_one, time_beach_one, inflow_beach_one)
            elif Hotel == "Three Star": 
                optimization_function_time(budget, time_constraint, nodes_beach_three, arcs_beach_three, cost_beach_three, time_beach_three, inflow_beach_three)
            else : 
                optimization_function_time(budget, time_constraint, nodes_beach_five, arcs_beach_five, cost_beach_five, time_beach_five, inflow_beach_five)

        
        elif x == "Winter Sports": 
            
            if Hotel == "One Star": 
                optimization_function_time(budget, time_constraint, nodes_wintersports_one, arcs_wintersports_one, cost_wintersports_one, time_wintersports_one, inflow_wintersports_one)
            elif Hotel == "Three Star": 
                optimization_function_time(budget, time_constraint, nodes_wintersports_three, arcs_wintersports_three, cost_wintersports_three, time_wintersports_three, inflow_wintersports_three)
            else : 
                optimization_function_time(budget, time_constraint, nodes_wintersports_five, arcs_wintersports_five, cost_wintersports_five, time_wintersports_five, inflow_wintersports_five)
                
        
        else:
            
            if Hotel == "One Star": 
                optimization_function_time(budget, time_constraint, nodes_others_one, arcs_others_one, cost_others_one, time_others_one, inflow_others_one)
            elif Hotel == "Three Star": 
                optimization_function_time(budget, time_constraint, nodes_others_three, arcs_others_three, cost_others_three, time_others_three, inflow_others_three)
            else: 
                optimization_function_time(budget, time_constraint, nodes_others_five, arcs_others_five, cost_others_five, time_others_five, inflow_others_five)
                
#--------------------The below commented section was for multi-objective optimization with weighted sum method --------#
    
    elif Answer == "Both": 
        
        mu_1 = float(input("How much importance you want to give on your money? [Enter anything between 0 to 1] "))

        mu_2 = float(input("How much importance you want to give on your time? [Enter anything between 0 to 1] "))
        
        if x == "Hiking":
            
            if Hotel == "One Star": 
                multi_optimization_function(budget, time_constraint,  nodes_hiking_one, arcs_hiking_one, cost_hiking_one, time_hiking_one, inflow_hiking_one)
            elif Hotel == "Three Star": 
                multi_optimization_function(budget, time_constraint, nodes_hiking_three, arcs_hiking_three, cost_hiking_three, time_hiking_three, inflow_hiking_three)
            else: 
                multi_optimization_function(budget, time_constraint, nodes_hiking_five, arcs_hiking_five, cost_hiking_five, time_hiking_five, inflow_hiking_five)
        
        elif x == "Beach":
            
            if Hotel == "One Star": 
                multi_optimization_function(budget, time_constraint, nodes_beach_one, arcs_beach_one, cost_beach_one, time_beach_one, inflow_beach_one)
            elif Hotel == "Three Star": 
                multi_optimization_function(budget, time_constraint, nodes_beach_three, arcs_beach_three, cost_beach_three, time_beach_three, inflow_beach_three)
            else: 
                multi_optimization_function(budget, time_constraint, nodes_beach_five, arcs_beach_five, cost_beach_five, time_beach_five, inflow_beach_five)

        
        elif x == "Winter Sports": 
            
            if Hotel == "One Star": 
                multi_optimization_function(budget, time_constraint, nodes_wintersports_one, arcs_wintersports_one, cost_wintersports_one, time_wintersports_one, inflow_wintersports_one)
            elif Hotel == "Three Star": 
                multi_optimization_function(budget, time_constraint, nodes_wintersports_three, arcs_wintersports_three, cost_wintersports_three, time_wintersports_three, inflow_wintersports_three)
            else: 
                multi_optimization_function(budget, time_constraint, nodes_wintersports_five, arcs_wintersports_five, cost_wintersports_five, time_wintersports_five, inflow_wintersports_five)
                
        
        else:
            
            if Hotel == "One Star": 
                multi_optimization_function(budget, time_constraint, nodes_others_one, arcs_others_one, cost_others_one, time_others_one, inflow_others_one)
            elif Hotel == "Three Star": 
                multi_optimization_function(budget, time_constraint, nodes_others_three, arcs_others_three, cost_others_three, time_others_three, inflow_others_three)
            else : 
                multi_optimization_function(budget, time_constraint, nodes_others_five, arcs_others_five, cost_others_five, time_others_five, inflow_others_five)
  

else: 
    
    print("Please modify your budget !!")
        
        
     

