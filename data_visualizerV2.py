# Created by Alexi De Avila Cadena
#
# libraries used for data visualization
# Version 2, need to add user-inputted
# files from terminal
#

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#path = r"C:\Users\Alexi\Documents\dataES\10eV50degs0edited.ON1" # easier to write once

counts = [] # comes from data file
scans = [] # created later using length of counts
path = r"C:\Users\Alexi\Documents\dataES" #defaults to some path on my PC

def welcomeMessage():
    print("Created by Alexi De Avila Cadena\n")

    print("Welcome to my program! This programs aims to visualize data")
    print("which the user specifies. Please place the data file in the")
    print("documents folder dataES. And make sure the data  file has")
    print(" no spaces in it. Make sure to add the file extension.")

welcomeMessage()

# I use a loop so that the program can be used over and over again without needing to exit
while True:
    newpath = input("Enter the name of the file: ")
    path = path + "\\" + newpath

    print("The new path is:", path)
    option = input("Is this correct?(y/n): ")# error checking and confirmation
    
    if option == 'y':
        print("Analyzing Data...")
        # opens the file object dataFile, reads and stores into a list/array of counts
        with open(path,'r') as dataFile:
            for line in dataFile:
                counts.append(line)
            
        # creates our scans file based on the counts    
        for x in range(len(counts)):
            scans.insert(x,x)

        counts = list(map(int, counts)) # makes sure our data is only integers

        # both of our x and y values must be the same type/length, both arrays/lists
        x = scans
        y = counts

        fix, ax = plt.subplots()
        ax.scatter(x, y, marker='o', color='red') # formatting of the plot
        ax.set_title("Elastic and Vibrational Peaks")
        ax.set_xlabel("Scans")
        ax.set_ylabel("Counts")
        ax.set_box_aspect(1)
        plt.show()
        option = input("Would you like to analyze more data?(y/n): ")
        if option == 'y':
            continue
        else:
            break
    
    else:
        option = input("Would you like to try again?(y/n) " )
        if option == 'y':
            continue
        else:
            print("Bye!")
            break
        
