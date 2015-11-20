import cv2
import numpy as np
filename = input("Type the file path of the desired map (.png only!): ")
img = cv2.imread(filename)
height, width, channel = img.shape #height and width of the image are necessary values

def polygon(x, y): #this function uses ray-casting to  determine if point (x,y) is within an obstacle
    counter = 0
    for i in range(x,width-1):
        colour = (img.item(y, i, 0), img.item(y, i, 1), img.item(y, i, 2)) #keeps track of the current pixel colour
        if (img.item(y, i+1, 0), img.item(y, i+1, 1), img.item(y, i+1, 2)) != colour: #if the next pixel is of a different colour, an edge has been met
          counter += 1 #keeps track of how many edges have been met

    #the parity of the counter determines whether point (x,y) is within an obstacle
    if counter % 2 == 0: #if even, point (x, y) is not in any obstacles
        return False
    elif counter % 2 != 0: #if odd, it is
        return True

coordinate_dictionary = {}
coordinate_list = []
counter = 0
for i in range(0,width+1,12): #these are columns
    for j in range(0,height+1,12): #these are rows
        if polygon(i,j) == False: #if point not in obstacle:
            counter += 1 #to keep track of the number of nodes
            img[j,i] = [0,0,255] #placing a red pixel on where the nodes will be
            coordinate_list.append((i,j))
counter2 = 0
for i in coordinate_list:
    counter2 += 1
    coordinate_dictionary["c"+str(counter2)] = i #gives a name to every node: c1, c2...

print(coordinate_dictionary) #these are the values returned by the algorithm, used later by the Dijkstra's algorithm




##UNCOMMENT THIS TO SEE A VISUAL REPRESENTATION OF THE NODES IN THE DICTIONARY
#A walkable space defined by red dots should be visible in a new window.

##cv2.imshow('Walkable Space defined by Nodes',img)
##
##if cv2.waitKey(0) & 0xff == 27:
##    cv2.destroyAllWindows()
##
##cv2.waitKey(0)

