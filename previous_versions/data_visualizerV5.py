# Created by Alexi De Avila Cadena
# 
# created more options I think
#

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

counts = [] # comes from data file
newcounts = [] # will be used to only get only numbers
scans = [] # created later using length of counts
path = r"C:\Users\Alexi\Documents\dataES" # defaults to some folder

def graphShower(x,y,titleNew,userXl,userYl,userYli,userXli):
    fix, ax = plt.subplots()
    ax.scatter(x, y, marker='o', color='red') # formatting of the plot
    ax.set_title(titleNew)
    ax.set_xlabel(userXl)
    ax.set_ylabel(userYl)
    ax.set_ylim(0,userYli)
    ax.set_xlim(0,userXli)
    ax.set_box_aspect(0.5)
    plt.show()

def welcomeMessage():
    print("Created by Alexi De Avila Cadena\n")

    print("Welcome to my program! This programs aims to visualize data")
    print("which the user specifies. Please place the data file in the")
    print("same folder as the exe. And make sure the data file has no")
    print("spaces in it. Make sure to add the file extension.")

def helpMessage():
    print("Y-Axis Max: yax")
    print("X-Axis Max: xax")
    print("Title: t")
    print("Y-Axis Label Change: yaxl")
    print("X-Axis Label Change: xaxl")
    print("Changes done: done")

# this function finds the biggest data point and returns it for the 
# default value of the max value on the y-axis
def findingMax(x):
    tempMax = 1
    for i in range(len(x)-1):
        if x[i] > tempMax and (i)!=len(x):
            tempMax = x[i]
            continue
        if x[i] == x[i]:
            continue
        if tempMax > x[i]:
            break
        else:
            continue
    return int(tempMax)

welcomeMessage()

userXlim = 0
userYlim = 0
option1 = ''
userXlabel = ''
userYlabel = ''
titleGraph = ''
option = ''

# I use a loop so that the program can be used over and over again without needing to exit
while True and option!='n':
    newpath = input("Enter the name of the file: ")
    path = path + "\\" + newpath
    
    print("The name of the file is:", path)
    option = input("Is this correct?(y/n): ")# error checking and confirmation
    option = option.lower()
    
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
        
        # User can change how graph looks, if the default, then nothing changes
        if option1 == '':
            userXlim = len(newcounts)+1
            userYlim = findingMax(newcounts) + 50
        
        if option1 == '':
            userXlabel = "Scans"
            userYlabel = "Counts"
        
        if option1 == '':
            titleGraph = "Elastic and Vibrational Peaks"
        
        graphShower(x,y,titleGraph,userXlabel,userYlabel,userYlim,userXlim)
        
        #use another loop to allow changes of the graph but uses the same one
        while True:
            option1 = input("Would you like to analyze more data or would you like to change something?(y/n): ")
            option1 = option1.lower()
            if option1 == 'y':
                option1 = input("What would you like to change? (Use h for Help): ")
                if option1 == 'h':
                    helpMessage()
                    continue
                if option1 == 'yax':
                    userYlim = int(input("Please enter the max number: "))
                    continue
                if option1 == 'xax':
                    userXlim = int(input("Please enter the max value: "))
                    continue
                if option1 == 't':
                    titleGraph = input("Please enter the new title: ")
                    continue
                if option1 == 'xaxl':
                    userXlabel = input("Please enter a new X-Axis Label: ")
                    continue
                if option1 == 'yaxl':
                    userYlabel = input("Please put a new Y-Axis Label: ")
                    continue
                if option1 == 'done':
                    break
                else:
                    print("Invalid Option!")
                    continue
            if option1 == 'done':
                graphShower(x,y,titleGraph,userXlabel,userYlabel,userYlim,userXlim)
                continue
            if option1 == 'n':
                print("Thank you for using my program! Bye!")
                break
            else:
                print("Invalid Option!")
                continue
        break
            
            
    if option == 'n':
        option = input("Would you like to try again?(y/n) " )
        while True: 
            if option == 'y':
                continue
            if option == 'n':
                print("Bye!")
                break
            else:
                print("Invalid Option!")
                continue
    else:
        print("Invalid Option!")
        continue