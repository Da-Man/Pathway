import cv2
import numpy as np
 
global height
global width
global channel
 
filename = 'testmap.png'
img = cv2.imread(filename)
if img is not None:
    print("Image loaded sucessfully!")
height, width = img.shape[:2] #height and width of the image are necessary values
 
def polygon(x, y):
    '''Checks if point (x, y) on the image is within an obstacle or not. Returns true if it is'''
    counter = 0 #keeps track of how many edges have been met
    for i in range(x,width-1):
        colour = (img.item(y, i, 0), img.item(y, i, 1), img.item(y, i, 2)) #keeps track of the current pixel colour
        if (img.item(y, i+1, 0), img.item(y, i+1, 1), img.item(y, i+1, 2)) != colour: #if the next pixel is of a different colour, an edge has been met
          counter += 1  
 
    #the parity of the counter determines whether point (x,y) is within an obstacle
    if counter % 2 == 0: #if even, point (x, y) is not in any obstacles
        return False
    elif counter % 2 != 0 and counter != 0: #if odd, it is
        return True
 
 
coordinate_dictionary = {} #holds tuples of (x,y) values for all traversable nodes with numbered names
wall_list = [] #holds tuples of (x,y) for all untraversible points found by polygon(x,y)
walkable = [] #holds tuples of (x,y) values for all traversable nodes
counter = 0 #used to number walkable nodes
 
for i in range(0,width+1,20): #these are columns
    for j in range(0,height+1,20): #these are rows
        if polygon(i,j) == False: #if point not in obstacle:
            img[j,i] = [0,0,255]
            walkable.append((i,j))
        else:
            wall_list.append((i/20,j/20))
 
for i in walkable:
    counter += 1
    coordinate_dictionary["c"+str(counter)] = i #numbering/naming the walkable nodes