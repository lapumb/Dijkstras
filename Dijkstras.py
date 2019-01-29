# @author Blake Lapum
# MTH 325-03
# Winter 2018
# Dijkstra's Project


# Takes a weighted graph and returns the sum of all the weights + 1
def infty(graph):
    weight = 0
    # Looping through the key values in graph dict
    for index in graph:
        # Looping through inner index's within index
        for inner in graph[index]:
            # Looping through very inner lists within index
            for num in inner:
                # Checking if the list element is an int
                if isinstance(num, int):
                    # If so, add the weight to the total weight
                    weight += num
    # Since we added every weight twice (once for each vertex),
    # add total weight into total & divide by 2, then add 1
    total = int(weight / 2) + 1
    # Return the total
    return total


# Takes weighted graph and returns vertex coloring such that "A"
# is colored with 0 and all other vertices are colored with infty
def initial(graph):
    # Initialize an empty dict
    init = {}
    # Loop through key values in the graph dict
    for index in graph:
        # If vertex "A", color = 0
        if index == 'A':
            init[index] = 0
        # Else, color the vertex infty
        else:
            init[index] = infty(graph)
    # Return new dict init
    return init


# Takes a vertex-coloring and list of vertices, returns smallest vertex color
def find_min(color, queue):
    # Initialize new dict smallest
    smallest = {}
    # Loops through keys in queue
    for index in queue:
        # If the key is found in color
        if index in color:
            # Add the key and it's coloring to smallest dict
            smallest[index] = color[index]
    # Returns minimum value within smallest dict
    return min(smallest, key=smallest.get)


# Takes in a weighted graph and returns vertex coloring of
# Dijkstra's algorithm, with "A" as the source
def dijkstra(graph):
    # initialize a new dict to initial values ("A" = 0, all others = sum+1)
    color = initial(graph)
    # loop through each index in graph
    for index in graph:
        # loop through each vertices neighbors
        for neighbor in graph[index]:
            # check if color + second neighbor is less than current color value
            if color[index] + neighbor[1] < color[neighbor[0]]:
                # if so, reset the color value to color + neighbor
                color[neighbor[0]] = color[index] + neighbor[1]
    # return new dictionary with dijkstra's algorithm applied
    return color


# Takes a weighted graph and determines whether it's connected or not
def is_connected(graph):
    # initializing return variable to true
    connected = True
    # setting inf variable to infty max value
    inf = infty(graph)
    # setting color to proper dijkstra coloring
    color = dijkstra(graph)
    # loop through color graph
    for i in color:
        # check if each instance is >= to max value
        if color[i] >= inf:
            # if so, it must not be connected
            connected = False
    # return connected value
    return connected


# Dict to test infty, initial, dijkstra, is_connected
test = {
    "A": [["B", 10], ["D", 5]],
    "B": [["A", 10], ["C", 5]],
    "C": [["B", 5], ["D", 15]],
    "D": [["C", 15], ["A", 5]]
}

# dict to test dijkstra 2, connected 2
dijkcon = {
    "A": [["B", 10], ["D", 5]],
    "B": [["A", 10], ["C", 5]],
    "C": [["B", 5], ["D", 15]],
    "D": [["C", 15], ["A", 5]],
    "E": [["F", 5]],
    "F": [["E", 5]]
}

# dict to test find_min
coloring = {
    "A": 0,
    "B": 10,
    "C": 10,
    "D": 15
}

# testing functions based on project descriptions
print("infty:" + str(infty(test)))
print("initial: " + str(initial(test)))
print("find_min: " + find_min(coloring, ["A", "D"]))
print("find_min 2: " + find_min(coloring, ["B", "C", "D"]))
print("dijkstra: " + str(dijkstra(test)))
print("dijkstra 2: " + str(dijkstra(dijkcon)))
print("is_connected: " + str(is_connected(test)))
print("is_connected 2: " + str(is_connected(dijkcon)))
