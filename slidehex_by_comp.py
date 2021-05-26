from math import *
from itertools import permutations

def find_neighbors(configt,board):
    """
    Add all neighbors of a sliding-puzzle configuration to a list.
    
    Keyword arguments:
    configt -- tuple representing a configuration of the board
    board -- list representing a hex board by coordinates of centers of hexes
    
    This function returns a list of all neighbors of the configuration configt
    which may be reached by sliding a single tile.
    """
    neighbors = []
    
    config=list(configt)  # convert from tuple to list--may not be needed    
    n=len(board) 
    zeros=[i for i in range(n) if config[i]==0] # list of holes on board
    
    # Iterate over tiles on the board.
    # Check for pairs of neighboring holes next to tile.
    # Perform both possible slides of tile into pairs of neighboring holes
    # Add resulting configurations to list of neighbors of configt.
    # Note: why not iterate over zeros instead? More efficient?
    for i in range(n): # iterate over tile positions
        if config[i]!=0: # check that tile is not a hole
            h=[]  # This will be list of zeros which neighbor the current tile
            for z in zeros:
                # check if a hole is next to current tile
                # if it is, add it to the list of neighboring holes
                if sqrt((board[i][0]-board[z][0])**2 + (board[i][1]-board[z][1])**2)<=1:
                    h.append(z)
            # Iterate over list of holes adjacent to current tile
            # Perform any possible slides
            # Add resulting new configurations to list of neighbors of tile
            for z in range(len(h)): 
                for zz in range(len(h)-z-1):
                    # Check if pair of holes neighboring our tile are adjacent
                    if sqrt((board[h[z]][0]-board[h[zz+z+1]][0])**2 + (board[h[z]][1]-board[h[zz+z+1]][1])**2)<=1:
                        # For each pair of adjacent holes, perform both
                        # possible slides of current tile into the holes
                        A=[config[col] for col in range(n)] 
                        B=[config[col] for col in range(n)]
                        A[i]=0 # Current tile becomes hole after slide
                        B[i]=0 # Current tile becomes hole
                        A[h[z]]=config[i] # Current tile into first hole
                        B[h[zz+z+1]]=config[i] # Current tile into second hole
                        # Add both new configurations to list of neighbors
                        # of our configuration configt
                        neighbors.append(tuple(A)) 
                        neighbors.append(tuple(B))
    return neighbors


#number of holes
k=2
board=((0,0),(0,1),(-1.5/sqrt(3),0.5),(-1.5/sqrt(3),1.5))

#3x3 paralelogram
#board=((0,0),(0,1),(0,2),(-1.5/sqrt(3),0.5),(-1.5/sqrt(3),1.5),(-1.5/sqrt(3),2.5),(-sqrt(3),1),(-sqrt(3),2),(-sqrt(3),3))

#Side 1 hexagon
#board=((0,0),(1,0),(-0.5,-1.5/sqrt(3)),(0.5,-1.5/sqrt(3)),(1.5,-1.5/sqrt(3)),(0,-sqrt(3)),(1,-sqrt(3)))

#Side 2 hexagon
#board=((-1,sqrt(3)),(0,sqrt(3)),(1,sqrt(3)),(-1.5,1.5/sqrt(3)),(-0.5,1.5/sqrt(3)),(0.5,1.5/sqrt(3)),(1.5,1.5/sqrt(3)),(-2,0),(-1,0),(0,0),(1,0),(2,0),(-1.5,-1.5/sqrt(3)),(-0.5,-1.5/sqrt(3)),(0.5,-1.5/sqrt(3)),(1.5,-1.5/sqrt(3)),(-1,-sqrt(3)),(0,-sqrt(3)),(1,-sqrt(3)))

#4x4 paralelogram
#board=((0,0),(1,0),(2,0),(3,0),(0.5,-1.5/sqrt(3)),(1.5,-1.5/sqrt(3)),(2.5,-1.5/sqrt(3)),(3.5,-1.5/sqrt(3)),(1,-sqrt(3)),(2,-sqrt(3)),(3,-sqrt(3)),(4,-sqrt(3)),(1.5,-4.5/sqrt(3)),(2.5,-4.5/sqrt(3)),(3.5,-4.5/sqrt(3)),(4.5,-4.5/sqrt(3)))


n=len(board) # Board is represented by list, entries are centers of tiles

def find_new(new_configs, found_already, comp_dict):
    next_up = []
    for config in new_configs:
        my_pals = find_neighbors(config, board)
        comp_dict[config] = my_pals
        for pal in my_pals:
            if not (pal in found_already):
                next_up.append(pal)
                found_already.append(pal)
    return(next_up)

def build_component(vertex):
    found = []
    on_deck = [vertex]
    comp_dict = {}
    while True:
        on_deck = find_new(on_deck, found, comp_dict)
        if on_deck == []:
            break
    return(comp_dict)

def find_new_idx(new_configs, found_already, comp_dict):
    next_up = []
    for config in new_configs:
        my_pals = find_neighbors(config, board)
        comp_dict[config] = my_pals
        for pal in my_pals:
            if not (pal in found_already):
                next_up.append(pal)
                found_already.append(pal)
    return(next_up)

def build_component_idx(vertex):
    found = []
    on_deck = [vertex]
    comp_dict = {}
    while True:
        on_deck = find_new(on_deck, found, comp_dict)
        if on_deck == []:
            break
    return(comp_dict)  
    
                
                
            
 




