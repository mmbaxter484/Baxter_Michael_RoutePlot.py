# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:01:04 20241

@author: mbaxter
"""

import matplotlib.pyplot as plt

global game_active
game_active = True

# Function for grid plotting
def plotting(x_coordinates, y_coordinates, x_start, y_start):
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    # Plot line between points
    plt.plot(x_coordinates, y_coordinates, label = '_nolegend_')
    
    # Plot individual coordinates as X
    plt.scatter(x_coordinates[1:-1], y_coordinates[1:-1], marker = 'x', c='black', label = '_nolegend_')
    
    # Plot start and finish points
    plt.scatter(x_start, y_start, c='red')
    plt.scatter(x_coordinates[-1], y_coordinates[-1], c='green')
    
    # Set axis limits
    ax.set_xlim(-0.5,12.5)
    ax.set_ylim(-0.5,12.5)
    
    # Set axis labels
    ax.set_xlabel("E & W")
    ax.set_ylabel("N & S")
    
    # Set legend
    plt.legend(['START','FINISH'])
    
    # Set grid lines to not overlap point positions
    ax.set_yticks([0,1,2,3,4,5,6,7,8,9,10,11,12], minor = False)
    ax.set_yticklabels(['0','1','2','3','4','5','6','7','8','9','10','11','12'], minor = False)
    ax.set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5], minor = True)
    ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11,12], minor = False)
    ax.set_xticklabels(['0','1','2','3','4','5','6','7','8','9','10','11','12'], minor = False)
    ax.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5], minor = True)
    ax.grid(True, which='minor')

    plt.show()
    
# Main function
def main():
    global game_active
    game_active = True

    # Get required input
    route = input("Enter the next route instructions file (1, 2, or 3), or enter STOP to finish: ")
    if route == '1' or route == '2' or route == '3':
        route = 'Route00'+route+'.txt'
    elif route == 'STOP':
        print('ENDING GAME')
        game_active = False
        return
    else:
        print('Not a suitable input, pick again.')
        main()
        return
    
    # Get route data        
    route_data = open(route)
    route_data = route_data.read()
    route_data = route_data.split('\n')
    
    x_start = int(route_data[0])
    y_start = int(route_data[1])
    
    x = x_start
    y = y_start
    
    coordinates = []
    coordinates.append([x_start, y_start])
    x_coordinates = []
    x_coordinates.append([x_start])
    y_coordinates = []
    y_coordinates.append([y_start])
      
    # Define commands for direction instructions
    for data in range(2,len(route_data)-1):
        if route_data[data] == 'N':
            y = y + 1
        elif route_data[data] == 'S':
            y = y - 1
        elif route_data[data] == 'E':
            x = x + 1
        else:
            x = x - 1
            
        if x < 1 or x > 12 or y < 1 or y > 12:
            print("Error: The route is outside of the grid")
            break
            
        coordinates.append([x,y])
        x_coordinates.append([x])
        y_coordinates.append([y])
        
    plotting(x_coordinates, y_coordinates, x_start, y_start)
        
    
while game_active == True:
    main()
