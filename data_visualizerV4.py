# Created by Alexi De Avila Cadena
#
# libraries used for data visualization
# Version 4, can now create executables
# so I need to make a universal version
# have to mess with the path option
#
# make a folder that the exe can read on
# main PC at work
#

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

counts = [] # comes from data file
newcounts = [] # will be used to only get only numbers
scans = [] # created later using length of counts
path = r"Some path:\orsomething" # defaults to its workspace

def welcomeMessage():
    print("Created by Alexi De Avila Cadena\n")

    print("Welcome to my program! This programs aims to visualize data")
    print("which the user specifies. Please place the data file in the")
    print("same folder as the exe. And make sure the data file has no")
    print("spaces in it. Make sure to add the file extension.")

welcomeMessage()

# I use a loop so that the program can be used over and over again without needing to exit
while True:
    newpath = input("Enter the name of the file: ")
    path = path + newpath

    print("The name of the file is:", path)
    option = input("Is this correct?(y/n): ")# error checking and confirmation
    
    # need to read file smarter by skipping some lines at beginning and end
    if option == 'y':
        print("Analyzing Data...")
        # opens the file object dataFile, reads and stores into a list/array of counts
        with open(path,'r') as dataFile:
            for line in dataFile:
                counts.append(line)
        dataFile.close()
        
        # this for loop makes a new list that only contains the numbers needed
        for d in range((len(counts)-17)): # 817-17 = 800
            k = d+13 # start at line 13 because before is strings
            newcounts.insert(d,counts[k]) # this will keep our numbers
        
        # creates our scans file based on the counts    
        for x in range(len(newcounts)):
            scans.insert(x,x)

        newcounts = list(map(int, newcounts)) # makes sure our data is only integers

        # both of our x and y values must be the same type/length, both arrays/lists
        x = scans
        y = newcounts

        fix, ax = plt.subplots()
        ax.scatter(x, y, marker='o', color='red') # formatting of the plot
        ax.set_title("Elastic and Vibrational Peaks")
        ax.set_xlabel("Scans")
        ax.set_ylabel("Counts")
        ax.set_box_aspect(0.5)
        plt.show()
        option = input("Would you like to analyze more data?(y/n): ")
        if option == 'y':
            continue
        else:
            print("Thank you for using my program! Bye!")
            break
    
    else:
        option = input("Would you like to try again?(y/n) " )
        if option == 'y':
            continue
        else:
            print("Bye!")
            break