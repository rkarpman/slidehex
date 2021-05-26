from math import *
from itertools import permutations

def configspace(configt,board,CS):
    """
    Add all neighbors of a sliding-puzzle configuration to the dictionary CS.
    
    Keyword arguments:
    configt -- tuple representing a configuration of the board
    board -- list representing a hex board by coordinates of centers of hexes
    CS -- a dictionary whose keys are all configurations of the board
          values are lists which start with two integer flags,
          and to which neighbors of the configuration confight are added.
    
    This function finds all neighbors of the configuration configt, and 
    which may be reached by sliding a single tile, and adds them to the 
    list corresponding to confight. 
    
    The first entry of the list
    indexed by the configt is set to 1 to indicate that neighbors of this
    configuration have been found and added to CS.
    
    A separate flag is set for all neighbors 
    of configt, to indicate that they are in the same connected component. 
    If no neighbors are found, this same flag is set of -1 for configt itself. 
    """
    
    CS[configt][0]=1  # indicates that neighbors of confight will be added
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
                        CS[configt].append(tuple(A)) 
                        CS[configt].append(tuple(B))
                        # For both neighbors found, change flag
                        # in their corresponding label in the dictionary config
                        # to indicate that they are in the same connected 
                        # component as the configuration configt.
                        CS[tuple(A)][1]=CS[configt][1]
                        CS[tuple(B)][1]=CS[configt][1]
    # If no neighors were found, set a flag to say that
    # this is an isolated configuration.
    if len(CS[configt])==2:
        CS[configt][1]=-1
    return(CS)

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

# List of possible configurations, zeros represent holes
P=tuple(set(permutations(tuple(range(1,n-k+1))+tuple(0 for col in range(k)))))
CS=dict.fromkeys(P) # Create dictionary indexed by configurations

# Set two integer flags which record whether we have found neighbors
# of configuration, and whether that configuration has been assigned
# to a component
for k in CS:
    CS[k]=[0,0]

# The integer c indexes the components of the graph
c=1
# Repeat while there are still configurations whose neighbors
# we haven't found yet.
while any(v[0]==0 for v in CS.values()):
    # This loop runs exactly once per component, followed by a break
    for config in CS:
    # Loop starts when we find a configuration config
    # which isn't already known to be a neighbor of another vertex.
        if CS[config][0]==0 and CS[config][1]==0:
            CS[config][1]=c
            # Search for all neigbors of current configuration.
            # Update second integer in that list with c, the component number.
            CS=configspace(config,board,CS)  
            print("made it through the first loop:", config, "c = ", c, "\n")
            break
    # The second loop finishes adding vertices to the new compoment,
    # labeled component c, whose first vertex was the configuration
    # found in the "for" loop above.
    # Start by asking if there are vertices in component c
    # whose neighbors haven't been found yet.
    while any(v[0]==0 and v[1]==c for v in CS.values()):
        # Each time this loop is called, it will exit after executing once.
        # If there are still vertices whose neighbors need to be found,
        # we re-enter the loop.
        for config in CS:
            if CS[config][0]==0 and CS[config][1]==c:
                CS=configspace(config,board,CS)
                break
    # If the last component we found was not an isolated component,
    #
    # Note that we're using the fact that index labels "leak"
    # into the body of the function.
    if CS[config][1]!=-1:
        c=c+1

# Create a list whose entries represent connected components
# A component represented by a subset of the dictionary CS
# whose keys are the configurations in that component.
comp=[1]*(c-1) #create a list with dummy values
for i in range(c-1): 
    comp[i]=dict((k,CS[k]) for k in CS if CS[k][1]==i+1)

# Create a file which lists our results.
# The file lists the number of components found with more than one configuration.
# Note that all components of more than one configurations
# contain the same number of configuations. (Todo: write down a proof of this.)
file=open("resultados.txt","w+")
# The length of the dictionary comp[i] is the number of
# configurations in the component i.
file.write("We found %d components with %d configurations each." %((c-1), len(comp[0])))
file.write("\n")
for i in range(c-1):
    file.write("\n")
    file.write("Component " + str(i+1) + ":\n")
    # Write each configuration and its list of neighbors
    # The two integer flags are omitted via list slicing
    for k in comp[i]:
        file.write(str(k)+" "+str(comp[i][k][2:])+"\n")
    file.write("\n")
file.close()



