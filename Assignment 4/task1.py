output_file = open("output1.txt", "w")
def readFile():
    # reading file from as input
    # change the file name according to yours
    f = open("input1.txt", "r")
    
    # first line of input contains the number of vertices in the graph
    n = f.readline()
    # strip() gets rid of the new line
    # try printing n without strip()
    # print(n.strip())
    n = n.strip()
    # print(type(n))
    # n is of type string. we need to convert it to int
    n=int(n)
    # print(type(n))
    
    # the second line of the file contains the number of connections
    c = f.readline()
    c = c.strip()
    c = int(c)
    # print(c)
    
    buildGraphUsingDictionary(c,f)
    f.seek(0)
    buildGraphUsingListofLists(c,f)
    


# we want to build an adjacency list like the following
# A -> B,C 
# One vertex can be connected to multiple vertices
# which means multiple values are associated with one vertex
# one data structure that can be used is a dictionary of lists
# {A:[B,C]}

def buildGraphUsingDictionary(c,f): 
    # creating a dictionary
    graph = {}
    # the following lines of the file contain the connections
    # creating a directed graph (a,b means a is connected to b)
    
    counter = 0
    while (counter<c):
        line = f.readline() # reading each line
        a,b = line.split(",") # splitting the vertices
        b = b.strip() # getting rid of \n from the end
        
        # we first search if the value inside variable a exists in the dictionary or not
        if(a in graph):
            # if yes, then append() the value in b to a
            graph[a].append(b)
        else:
            # create a new list in graph with a as the key and b as the value
            graph[a] = [b]
        # print(a)
        # print(b)
        counter+=1    
    
    print(graph)
    printGraph(graph, None)
       
    
# TO DO
# This method must be completed by you
# You should code in such a way that the output should be
 # 1 -> 2,4
 # 2 -> 4
 # 3 -> 1,4
 # 4 -> 2
# notice this method takes both the graphs as parameters
# this means you have print the same output in the same style for both the datastructures
# if graph is none then print from listGraph
# if listGraph is none then print from graph
def printGraph(graph,listGraph):  
    # Your code
    global output_file
    if listGraph == None:
        for key, val in sorted(graph.items()):
            # print(f"{key} -> {val}\n", file= output_file)
            print(f"{key} -> ", file= output_file, end="")
            for i in range(len(val)):
                if i != len(val) -1:
                    print(f"{val[i]},", file= output_file, end="")
                else:
                    print(f"{val[i]}", file=output_file)
        print(file=output_file)
        
        
    elif graph == None:
        for i in range(len(listGraph)):
            if len(listGraph[i]) != 0:
                print(f"{i} -> ", file= output_file, end="")
            for j in range(len(listGraph[i])):
                if j != len(listGraph[i]) -1:
                    print(f"{listGraph[i][j]},", file= output_file, end="")
                else:
                    print(f"{listGraph[i][j]}", file= output_file)
        print(file=output_file)

# TO DO
# I have shown you how to build a graph using a dictionary of list
# now your job is to build a graph using list of lists [[E,B],[C,D]]
# it means A -> E,B and B -> C,D
def buildGraphUsingListofLists(c,f):
    # your code
    f.readline()
    f.readline()
    counter = 0
    max_val = -1
    while (counter<c):
        line = f.readline() # reading each line
        # print(line)
        a,b = line.split(",") # splitting the vertices
        
        if int(a) > max_val:
          max_val = int(a)
        counter += 1

    listGraph = [[]for i in range(max_val+1)]
    f.seek(0)
    f.readline()
    f.readline()
    
    counter = 0
    while (counter<c):
        line = f.readline() # reading each line
        # print(line)
        a,b = line.split(",") # splitting the vertices
        b = b.strip() # getting rid of \n from the end
        
        listGraph[int(a)].append(b)
        counter += 1
        print(listGraph)
    
    printGraph(None,listGraph)
    
# ======================Program starts here.========================

# read file using the readFile() method
readFile()
output_file.close()