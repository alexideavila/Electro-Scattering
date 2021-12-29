#libraries used for data visualization
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

path = r"C:\Users\Alexi\Documents\data_visualizations\short10eV.txt" # easier to write once
counts = [] # comes from data file
scans = [] # created later using length of counts

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
ax.scatter(x, y, marker='o', color='red')
ax.set_xlabel("Scans")
ax.set_ylabel("Counts")
ax.set_box_aspect(1)
plt.show()